from kata.roman_to_integer import Solution

def test_three():
    foo = Solution()
    assert foo.romanToInt("III") == 3

def test_four():
    foo = Solution()
    assert foo.romanToInt("IV") == 4

def test_fifty_eight():
    foo = Solution()
    assert foo.romanToInt("LVIII") == 58

def test_nineteen_ninety_four():
    foo = Solution()
    assert foo.romanToInt("MCMXCIV") == 1994
