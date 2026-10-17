class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need = {}

        for index, elem in enumerate(nums):
            needed = target - elem
            need[needed] = index

        for index, num in enumerate(nums):
            if num in need and index != need[num]:
                return [index, need[num]]

        