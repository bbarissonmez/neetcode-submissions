class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        min_product = nums[0]
        max_product = nums[0]

        result = nums[0]

        for i in range(1, len(nums)):
            can1 = nums[i]
            can2 = min_product * nums[i]
            can3 = max_product * nums[i]

            min_product = min(can1,can2,can3)
            max_product = max(can1,can2,can3)
            result = max(result, max_product)


        return result

        
