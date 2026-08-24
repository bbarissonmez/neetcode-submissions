class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        LEFT_BORDER = -1
        RIGHT_BORDER = len(s)

        def expand(left, right):
            while (left > LEFT_BORDER and right < RIGHT_BORDER and s[left] == s[right]):
                left -= 1
                right += 1

            return s[left+1:right]

        longest = ""
        for i in range(len(s)):
            s1 = expand(i, i)
            s2 = expand(i, i+1)

            if len(s1) > len(longest):
                longest = s1

            if len(s2) > len(longest):
                longest = s2

        return longest