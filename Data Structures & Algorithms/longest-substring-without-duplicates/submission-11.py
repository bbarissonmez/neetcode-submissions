class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        max_count = 0
        
        for r in range (len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)

            mp[s[r]] = r
            count = r - l + 1
            max_count = max (count, max_count)

        return max_count



            


