class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        difference_dict = {} # The difference and its index as a key-value pair

        index_counter = 0
        for num in nums:
            difference = target - num

            if difference in difference_dict:
                return [difference_dict[difference], index_counter]
            else:
                difference_dict[num] = index_counter

            index_counter += 1
        