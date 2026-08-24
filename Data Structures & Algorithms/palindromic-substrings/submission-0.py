class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1

        LEFT_BORDER = 0
        RIGHT_BORDER = len(s) - 1
        counter = 0

        def expand(left, right):
            nonlocal counter
            while (left >= LEFT_BORDER and right <= RIGHT_BORDER and s[left] == s[right]):
                left -= 1
                right += 1
                counter += 1

        for i in range(len(s)):
            # Odd palindrome
            expand(i, i)

            # Even palindrome
            expand(i, i+1)

        return counter


        