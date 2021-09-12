from kata.longest_common_prefix import Solution

def test_no_common_prefix():
    data = ["dog","racecar","car"]
    assert(Solution.longestCommonPrefix(data) == "")


def test_wee_common_prefix():
    data = ["flower","flow","flight"]

    assert(Solution.longestCommonPrefix(data) == "fl")
