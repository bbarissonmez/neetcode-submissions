class Solution:
    def search(self, nums: List[int], target: int) -> int:
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

        cutIndex = l

        num1 = self.binSearch(nums[:cutIndex], target)
        num2 = self.binSearch(nums[cutIndex:], target)

        if (num1 != -1):
            return num1
        elif (num2 != -1):
            return num2 + cutIndex
        else:
            return -1

    def binSearch(self, bin_list: List[int], target: int) -> int:
        l = 0
        r = len(bin_list) - 1

        while l <= r:
            mid = (l + r) // 2

            if (bin_list[mid] == target):
                return mid
            
            if (bin_list[mid] > target):
                r = mid - 1 
            else:
                l = mid + 1

        return -1