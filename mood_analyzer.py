# mood_analyzer.py
"""
Rule based mood analyzer for short text snippets.

This class starts with very simple logic:
  - Preprocess the text
  - Look for positive and negative words
  - Compute a numeric score
  - Convert that score into a mood label
"""

from typing import List, Dict, Tuple, Optional

from dataset import POSITIVE_WORDS, NEGATIVE_WORDS, NEGATION_WORDS


class MoodAnalyzer:
    """
    A very simple, rule based mood classifier.
    """

    def __init__(
        self,
        positive_words: Optional[List[str]] = None,
        negative_words: Optional[List[str]] = None,
    ) -> None:
        # Use the default lists from dataset.py if none are provided.
        positive_words = positive_words if positive_words is not None else POSITIVE_WORDS
        negative_words = negative_words if negative_words is not None else NEGATIVE_WORDS

        # Store as sets for faster lookup.
        self.positive_words = set(w.lower() for w in positive_words)
        self.negative_words = set(w.lower() for w in negative_words)
        self.negation_words = set(w.lower() for w in NEGATION_WORDS)

    # ---------------------------------------------------------------------
    # Preprocessing
    # ---------------------------------------------------------------------

    def preprocess(self, text: str) -> List[str]:
        """
        Convert raw text into a list of tokens the model can work with.

        TODO: Improve this method.

        Right now, it does the minimum:
          - Strips leading and trailing whitespace
          - Converts everything to lowercase
          - Splits on spaces

        Ideas to improve:
          - Remove punctuation
          - Handle simple emojis separately (":)", ":-(", "🥲", "😂")
          - Normalize repeated characters ("soooo" -> "soo")
        """
        cleaned = text.strip().lower().replace("'", "")
        tokens = cleaned.split()
        cleaned_tokens = [token.strip(".,!?;:()[]{}\"") for token in tokens]

        return cleaned_tokens

    # ---------------------------------------------------------------------
    # Scoring logic
    # ---------------------------------------------------------------------

    def _analyze_tokens(self, text: str) -> Tuple[List[str], List[str]]:
        """
        Shared helper: walk the tokens once and bucket them into
        positive_hits / negative_hits, accounting for negation words
        ("not", "never", "isnt", ...) that flip the sentiment of the
        word(s) that follow. Each negation word toggles the flip, so
        "not not happy" ends up positive again.
        """
        tokens = self.preprocess(text)
        positive_hits: List[str] = []
        negative_hits: List[str] = []
        negated = False

        for token in tokens:
            if token in self.negation_words:
                negated = not negated
                continue
            if token in self.positive_words:
                if negated:
                    negative_hits.append(f"not {token}")
                else:
                    positive_hits.append(token)
            if token in self.negative_words:
                if negated:
                    positive_hits.append(f"not {token}")
                else:
                    negative_hits.append(token)

        return positive_hits, negative_hits

    def score_text(self, text: str) -> int:
        """
        Compute a numeric "mood score" for the given text.

        Positive words (and negated negative words) increase the score.
        Negative words (and negated positive words) decrease the score.
        """
        positive_hits, negative_hits = self._analyze_tokens(text)
        return len(positive_hits) - len(negative_hits)

    # ---------------------------------------------------------------------
    # Label prediction
    # ---------------------------------------------------------------------

    def predict_label(self, text: str) -> str:
        """
        Turn a piece of text's sentiment hits into a mood label.

        Mapping:
          - both positive and negative words present -> "mixed"
          - more positive hits than negative          -> "positive"
          - more negative hits than positive          -> "negative"
          - no sentiment words at all                 -> "neutral"

        "Mixed" is based on whether both signals fired at all, not on
        whether they happen to cancel out to a net score of zero. That
        way "tired but hopeful" is "mixed" instead of "neutral", which
        is reserved for text with no sentiment words (e.g. "This is fine").
        """
        positive_hits, negative_hits = self._analyze_tokens(text)
        if positive_hits and negative_hits:
            return "mixed"
        elif len(positive_hits) > len(negative_hits):
            return "positive"
        elif len(negative_hits) > len(positive_hits):
            return "negative"
        else:
            return "neutral"

    # ---------------------------------------------------------------------
    # Explanations (optional but recommended)
    # ---------------------------------------------------------------------

    def explain(self, text: str) -> str:
        """
        Return a short string explaining WHY the model chose its label.

        TODO:
          - Look at the tokens and identify which ones counted as positive
            and which ones counted as negative.
          - Show the final score.
          - Return a short human readable explanation.

        Example explanation (your exact wording can be different):
          'Score = 2 (positive words: ["love", "great"]; negative words: [])'

        The current implementation is a placeholder so the code runs even
        before you implement it.
        """
        positive_hits, negative_hits = self._analyze_tokens(text)
        score = len(positive_hits) - len(negative_hits)

        return (
            f"Score = {score} "
            f"(positive: {positive_hits or '[]'}, "
            f"negative: {negative_hits or '[]'})"
        )
