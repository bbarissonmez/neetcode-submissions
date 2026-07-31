class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)

        l = 0 # First index
        r = n - 1 # Last index

        while (l < r):
            while not s[l].isalnum() and l < r:
                l += 1

            while not s[r].isalnum() and l < r:
                r -= 1

            if (s[l].lower() != s[r].lower()):
                print(s[l] ,s[r], l, r)
                return False

            l += 1
            r -= 1

        return True
