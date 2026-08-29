class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}

        def dfs(index, previous_index):
            if index == len(nums):
                return 0

            key = (index, previous_index)
            
            if key in cache:
                return cache[key]
            
            if (previous_index == -1 or nums[index] > nums[previous_index]):
                # We can include it in the subsequence
                include = 1 + dfs(index+1, index)

                # We dont include it in the subequence
                dont_include = dfs(index+1, previous_index)
                cache[key] = max(include, dont_include)

            else:
                cache[key] = dfs(index+1, previous_index)

            return cache[key]

        return dfs(0, -1)