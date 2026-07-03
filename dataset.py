"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
]

# Words that flip the sentiment of the word(s) that follow them
# (e.g. "not happy", "isn't bad", "don't hate").
NEGATION_WORDS = [
    "not",
    "no",
    "never",
    "isnt",
    "arent",
    "wasnt",
    "werent",
    "dont",
    "doesnt",
    "didnt",
    "cant",
    "cannot",
    "wont",
    "couldnt",
    "shouldnt",
    "wouldnt",
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"
]

# TODO: Add 5-10 more posts and labels.
#
# Requirements:
#   - For every new post you add to SAMPLE_POSTS, you must add one
#     matching label to TRUE_LABELS.
#   - SAMPLE_POSTS and TRUE_LABELS must always have the same length.
#   - Include a variety of language styles, such as:
#       * Slang ("lowkey", "highkey", "no cap")
#       * Emojis (":)", ":(", "🥲", "😂", "💀")
#       * Sarcasm ("I absolutely love getting stuck in traffic")
#       * Ambiguous or mixed feelings
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the lists:
#
# SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
# TRUE_LABELS.append("mixed")
#
# Remember to keep them aligned:
#   len(SAMPLE_POSTS) == len(TRUE_LABELS)

SAMPLE_POSTS.append("You didnt do terrible")
TRUE_LABELS.append("positive")

SAMPLE_POSTS.append("Today was alright 👍")
TRUE_LABELS.append("neutral")

SAMPLE_POSTS.append("Lowkey I am so tired of this")
TRUE_LABELS.append("negative")

SAMPLE_POSTS.append("It will be alright, I guess")
TRUE_LABELS.append("neutral")

SAMPLE_POSTS.append("On god this is the best day ever")
TRUE_LABELS.append("positive")

# "Breaker" sentences designed to confuse the rule based model:
# negation, sarcasm, slang/emoji, and cancelling/mixed sentiment.

SAMPLE_POSTS.append("I am so not excited about this")
TRUE_LABELS.append("negative")

SAMPLE_POSTS.append("Oh great, another Monday")
TRUE_LABELS.append("negative")

SAMPLE_POSTS.append("I love waiting an hour in line, truly amazing")
TRUE_LABELS.append("negative")

SAMPLE_POSTS.append("This isn't bad at all")
TRUE_LABELS.append("positive")

SAMPLE_POSTS.append("I don't hate it")
TRUE_LABELS.append("positive")

SAMPLE_POSTS.append("Not gonna lie, today was kind of a mess but also kind of fun")
TRUE_LABELS.append("mixed")

SAMPLE_POSTS.append("lowkey obsessed, no cap 🔥")
TRUE_LABELS.append("positive")

SAMPLE_POSTS.append("I could NOT be happier lol 😂")
TRUE_LABELS.append("positive")

SAMPLE_POSTS.append("Great, just great. Nothing ever goes wrong for me 🙃")
TRUE_LABELS.append("negative")

SAMPLE_POSTS.append("I'm fine. Really. I'm fine.")
TRUE_LABELS.append("negative")

SAMPLE_POSTS.append("This is the worst best day of my life")
TRUE_LABELS.append("mixed")

SAMPLE_POSTS.append("Bad? No, this was terrible")
TRUE_LABELS.append("negative")