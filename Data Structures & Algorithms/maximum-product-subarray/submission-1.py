class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        min_product = min(nums[1], nums[0] * nums[1])
        max_product = max(nums[1], nums[0] * nums[1])

        result = max(min_product, max_product)

        for i in range(2, len(nums)):
            can1 = nums[i]
            can2 = min_product * nums[i]
            can3 = max_product * nums[i]

            min_product = min(can1,can2,can3)
            max_product = max(can1,can2,can3)
            result = max(result, max_product)


        return result

        
