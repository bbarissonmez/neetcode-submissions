class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0

        for i in range(0, len(nums)+1):
            res ^= i

        for elem in nums:
            res ^= elem

        return res