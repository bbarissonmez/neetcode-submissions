from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1_dict = Counter(s1)
        num_matched = 0

        for r in range (len(s2)):
            if s1_dict[s2[r]] > 0:
                num_matched += 1

            s1_dict[s2[r]] -= 1

            if r - l + 1 > len(s1):
                if s1_dict[s2[l]] >= 0:
                    num_matched -= 1

                s1_dict[s2[l]] += 1
                l += 1
            
            if num_matched == len(s1):
                return True

        return False

