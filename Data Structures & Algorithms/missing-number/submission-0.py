class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        for elem in nums:
            total += elem

        n = len(nums)
        return (n*(n+1)//2) - total