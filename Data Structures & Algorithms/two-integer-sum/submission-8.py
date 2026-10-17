class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need = {}

        for index, elem in enumerate(nums):
            complement = target - elem
            
            if complement in need:
                return [need[complement], index]
            else:
                need[elem] = index

        return []

        