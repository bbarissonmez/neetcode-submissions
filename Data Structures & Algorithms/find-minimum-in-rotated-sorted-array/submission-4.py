class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        
        # This has now been rotated for sure
        l = 0
        r = len(nums) - 1

        while (l < r):
            mid = l + (r - l) // 2

            if nums[mid] < nums[r]: # Mid and r must be together, min either at r or to the left
                r = mid
            else: # Mid and l must be together, min to the right
                l = mid + 1
        return nums[r]
        