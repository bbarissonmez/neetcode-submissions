class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for num in nums:
            if num in seen.keys():
                return True
            else:
                seen[num] = 1

        return False
        