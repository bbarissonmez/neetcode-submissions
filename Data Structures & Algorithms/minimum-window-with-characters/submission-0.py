from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        l = 0
        target_dict = Counter(t)
        window_dict = {}

        result = ""
        min_length = float("inf")

        for r in range (len(s)):
            window_dict[s[r]] = 1 + window_dict.get(s[r], 0)

            while (all(k in window_dict and v <= window_dict[k] for k, v in target_dict.items())):
                window_length = r-l+1
                if (window_length < min_length):
                    min_length = window_length
                    result = s[l:r+1]
                
                window_dict[s[l]] -= 1
                l += 1


        return result

            

            

        