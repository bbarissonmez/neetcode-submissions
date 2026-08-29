class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [[None] * (n + 1) for _ in range(n)]

        def dfs(index, previous_index):
            if index == n:
                return 0

            prev_key = previous_index + 1

            if cache[index][prev_key] is not None:
                return cache[index][prev_key]

            if previous_index == -1 or nums[index] > nums[previous_index]:
                include = 1 + dfs(index + 1, index)
                dont_include = dfs(index + 1, previous_index)

                cache[index][prev_key] = max(include, dont_include)
            else:
                cache[index][prev_key] = dfs(index + 1, previous_index)

            return cache[index][prev_key]

        return dfs(0, -1)