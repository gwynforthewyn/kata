class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        
        for char in s:
          result += self.lookup(char)
        
        print(result)
        return result
        
    def lookup(self, candidate):
        romans = {
                  "I": 1,
                  "V": 5,
                  "X": 10,
                  "L": 50,
                  "C": 100,
                  "D": 500,
                  "M": 1000
                 }
        
        return romans[candidate]
        