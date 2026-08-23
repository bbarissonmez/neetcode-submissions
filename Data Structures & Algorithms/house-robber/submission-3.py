class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums) 

        def dp(index):
            if index >= len(nums):
                return 0

            if cache[index] == -1:
                robbed = nums[index] + dp(index+2)
                not_robbed = dp(index+1)
                cache[index] = max(robbed, not_robbed)

            return cache[index]

        return dp(0)

        
        