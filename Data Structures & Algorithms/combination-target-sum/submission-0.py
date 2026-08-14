class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, current, current_sum):
            if current_sum == target:
                result.append(current)
                return

            if i >= len(nums) or current_sum > target:
                return

            # choice 1: use nums[i]
            dfs(i, current+[nums[i]], current_sum+nums[i])

            # choice 2: don't use nums[i] anymore
            dfs(i+1, current, current_sum)

        dfs(0, [], 0)
        return result

        