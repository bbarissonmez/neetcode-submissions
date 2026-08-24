class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        nums1 = nums[:len(nums)-1]
        nums2 = nums[1:]

        if not nums1 or not nums2:
            return 0
        if len(nums2) == 1 or len(nums2) == 1:
            return max(nums1[0],nums2[0])

        dp1 = [0] * len(nums)
        dp1[0] = nums1[0]
        dp1[1] = max(nums1[0], nums1[1])

        for i in range(2, len(nums)-1):
            dp1[i] = max(dp1[i - 1], nums1[i] + dp1[i - 2])

        dp2 = [0] * len(nums)
        dp2[0] = nums2[0]
        dp2[1] = max(nums2[0], nums2[1])

        for i in range(2, len(nums)-1):
            dp2[i] = max(dp2[i - 1], nums2[i] + dp2[i - 2])

        return max(dp1[-2], dp2[-2])