from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = Counter()
        l = 0
        max_freq = 0
        max_window_length = 0

        for r in range(len(s)):
            freq[s[r]] += 1
            max_freq = max(max_freq, freq[s[r]])

            window_length = r - l + 1
            required_replacements = window_length - max_freq

            while required_replacements > k:
                freq[s[l]] -= 1
                l += 1

                window_length = r - l + 1
                required_replacements = window_length - max_freq

            max_window_length = max(
                max_window_length,
                r - l + 1
            )

        return max_window_length