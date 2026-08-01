class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None:
            return 0

        window_set = set()

        n = len(s)

        left, right = 0, 0
        max_window_length = 0

        for right in range(len(s)):
            while s[right] in window_set:
                window_set.remove(s[left])
                left += 1

            window_set.add(s[right])

            window_length = right - left + 1
            max_window_length = max(
                max_window_length,
                window_length
            )

        return max_window_length
            

        