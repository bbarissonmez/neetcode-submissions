class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prefix_arr, postfix_arr = [1] * len(nums), [1] * len(nums)
        prefix_prod, postfix_prod = 1, 1

        for i in range (1, len(nums)):
            prefix_prod *= nums[i-1]
            prefix_arr[i] = prefix_prod

        for i in range (len(nums) - 2, -1, -1):
            print(i)
            postfix_prod *= nums[i+1]
            postfix_arr[i] = postfix_prod

        for i in range (0, len(nums)):
            result.append(prefix_arr[i] * postfix_arr[i])

        return result
