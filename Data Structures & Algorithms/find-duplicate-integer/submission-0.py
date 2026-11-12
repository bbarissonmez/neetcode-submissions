class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mask = 0

        for num in nums:
            bit = num
            if mask & (1 << bit):
                return num

            mask |= (1 << bit)


