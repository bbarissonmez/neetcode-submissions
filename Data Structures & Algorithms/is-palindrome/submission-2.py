class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = [char.lower() for char in s if char.isalnum()]
        n = len(clean_s)

        for i in range (n):
            if (clean_s[i] != clean_s[n-i-1]):
                return False

            if (i == n // 2):
                break

        return True        