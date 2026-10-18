class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while (l < r):
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]: # pivot to the right
                l = mid + 1
            else: # pivot at mid or to the left
                r = mid

        pivot = l

        if nums[pivot] == target:
            return pivot

        if pivot == 0:
            return self.binary_search(nums, 0, len(nums)-1, target)

        if target >= nums[0]: # It is in the left half, since the first elem in a rotated array is always strictly greater than every elem in the right
            return self.binary_search(nums, 0, pivot, target)
        else: # It is in the right half
            return self.binary_search(nums, pivot, len(nums)-1, target)

    
    def binary_search(self, nums, left, right, target):       
        while (left <= right):
            mid = left + (right - left) // 2 
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return -1 

                    
