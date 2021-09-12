"""
Problem Statement
We have a bunch of stickers which say "twitter" and we decide to cut these up into their separate letters to make new words. So, for example, one sticker would give us the letters "T", "W", "I", "T", "T", "E", "R", which we could rearrange into other word[s] (like "write", "wit", "twit", etc)
 
Challenge:
Write a function that takes as its input an arbitrary string and as output, returns the number of intact “twitter” stickers we would need to cut up to recreate that string.
 
Example: twitter_stickers(“write wit twit”) would return "3", since we would need to cut up 3 stickers to provide enough letters to write “write wit twit”
"""

# How do you make a histogram of letters in a string?
# How do you find how many instances of the reference string you need?

# error check - what if the input contains invalid letters?

from collections import Counter


def twitter_stickers(input):

    reference_data = letter_frequencies("twitter")
    input_data = letter_frequencies(input)

    twitter_counterer = 1

    for letter in reference_data:
        while input_data[letter] > reference_data[letter] * twitter_counterer:
            twitter_counterer += 1

    return twitter_counterer


def letter_frequencies(input) -> dict:
    # letter_frequencies = {}
    # for letter in input:
    #     if letter not in letter_frequencies:
    #         letter_frequencies[letter] = 1
    #     else:
    #         letter_frequencies[letter] += 1

    letter_frequencies = Counter(input)
    return letter_frequencies


print(twitter_stickers("write wit twit"))
