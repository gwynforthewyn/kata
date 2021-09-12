# https://leetcode.com/problems/valid-parentheses/

class Solution:

  def isValid(self, s: str) -> bool:


    pairs = {"(": ")", "{": "}", "[": "]"}

    counts = {}

    #For looking up the index of a key
    #when we have the value
    pairs_keys = pairs.keys()
    pairs_values = pairs.values()

    for key in pairs_keys:
        counts[key] = 0

    for char in s:
        if char in pairs_keys:
            counts[char] +=1
        else:
            key_index = list(pairs_values).index(char)
            counts[list(pairs_keys)[key_index]] -= 1

    for total_count in counts.values():
        if total_count != 0:
            return False

    return True
