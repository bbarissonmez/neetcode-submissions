class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        nums_set = set(nums)
        longest_count = 0

        for num in nums_set:
            count = 0
            if (num - 1) not in nums_set: # A root
                while (num + 1) in nums_set:
                    count += 1
                    if (count > longest_count):
                        longest_count = count

                    num += 1

        return longest_count + 1

