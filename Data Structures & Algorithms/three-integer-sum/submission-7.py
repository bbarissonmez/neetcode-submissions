class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort() # Let's go with the two-pointer approach

        for index, elem in enumerate(nums):
            if elem > 0:
                break

            if index > 0 and nums[index] == nums[index - 1]:
                continue

            target = -1 * elem

            i = index + 1
            j = len(nums) - 1

            while (i < j):
                curr_total = nums[i] + nums[j]

                if curr_total < target:
                    i += 1
                elif curr_total > target:
                    j -= 1
                else:
                    triplets.append([elem, nums[i], nums[j]])
                    i += 1
                    j -= 1

                    while (i < j) and nums[i - 1] == nums[i]:
                        i += 1
                    while (i < j) and nums[j] == nums[j + 1]:
                        j -= 1

        return triplets

            



        
        