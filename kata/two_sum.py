class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        store = dict()

        for i, val in enumerate(nums):
            difference_of_target_and_current_element = target - val
            if difference_of_target_and_current_element not in store:
                store[val] = i
            else:
                return [store[difference_of_target_and_current_element],i]
