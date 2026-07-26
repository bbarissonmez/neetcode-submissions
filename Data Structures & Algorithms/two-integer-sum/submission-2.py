class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        difference_dict = {} # The difference and its index as a key-value pair

        for i, num in enumerate(nums):
            difference = target - num

            if difference in difference_dict:
                return [difference_dict[difference], i]
            else:
                difference_dict[num] = i

        return []

        