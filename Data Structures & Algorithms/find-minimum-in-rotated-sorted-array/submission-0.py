class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                # Minimum must be strictly right of mid
                l = mid + 1
            else:
                # Mid might itself be the minimum
                r = mid

        return nums[l]