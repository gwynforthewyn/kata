from kata import two_sum as ts

def test_two_sum_success():
    nums, target = [2,7,11,15], 9
    summer = ts.Solution()

    # assert summer.twoSum(nums, target) == [0,1]

    nums, target = [3,2,4], 6
    assert summer.twoSum(nums, target) == [1,2]

    nums, target = [3, 3], 6
    # assert summer.twoSum(nums, target) ==  [0, 1]


