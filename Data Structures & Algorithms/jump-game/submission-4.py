class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0

        for index, num in enumerate(nums):
            if index > farthest:
                return False

            farthest = max(farthest, index + num)

        return True