#https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:

      result = 0

      for i in range(len(s)):

        if (i != len(s)-1 and self.lookup(s[i]) < self.lookup(s[i + 1])):
          result -= self.lookup(s[i])
        else:
          result += self.lookup(s[i])
      
      return result
        
    def lookup(self, candidate):
        romans = {
                  "I" : 1,
                  "V" : 5,
                  "X" : 10,
                  "L" : 50,
                  "C" : 100,
                  "D" : 500,
                  "M" : 1000
                 }
        
        return romans[candidate]
        