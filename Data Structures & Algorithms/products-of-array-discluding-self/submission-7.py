class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_count = 0

        for num in nums:
            if num == 0:
                zero_count += 1
                num = 1

            total_product *= num

        if zero_count == 0:
            return [total_product // elem for elem in nums]
        elif zero_count == 1:
            return [0 if elem != 0 else total_product for elem in nums]
        else:
            return [0 for elem in nums]