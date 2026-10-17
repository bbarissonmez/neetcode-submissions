class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        window = set()
        l = 0
        max_count = 1
        
        for r in range (len(s)):
            while s[r] in window and l < r:
                window.remove(s[l])
                l += 1

            window.add(s[r])
            count = r - l + 1
            max_count = max (count, max_count)

        return max_count



            


