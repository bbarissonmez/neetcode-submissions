class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = [None] * len(nums)

        def dfs(index):
            if index == len(nums) - 1:
                return True
            elif index >= len(nums) -1:
                return False

            if cache[index] != None:
                return cache[index]

            
            flag = False
            for i in range (1, nums[index]+1):
                print(index, i, flag)
                if (dfs(index+i)):
                    flag = True
                    break

            cache[index] = flag
            return cache[index]

        return dfs(0)