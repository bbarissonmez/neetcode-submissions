class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)

        l = 0 # First index
        r = n - 1 # Last index

        while (l < r):
            while not self.alphaNum(s[l]) and l < r:
                l += 1

            while not self.alphaNum(s[r]) and l < r:
                r -= 1

            if (s[l].lower() != s[r].lower()):
                print(s[l] ,s[r], l, r)
                return False

            l += 1
            r -= 1

        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))