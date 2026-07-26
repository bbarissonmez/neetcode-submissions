class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_set, t_set = {}, {}

        for char in s:
            if char not in s_set:
                s_set[char] = 1
            else:
                s_set[char] += 1

        for char in t:
            if char not in t_set:
                t_set[char] = 1
            else:
                t_set[char] += 1

        return s_set == t_set

        