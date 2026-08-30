class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        result, max_product = nums[0], nums[0]

        for i in range(1, len(nums)):
            can1 = nums[i]
            can2 = max_product + nums[i]

            max_product = max(can1, can2)
            result = max(result, max_product)

        return result

        
        