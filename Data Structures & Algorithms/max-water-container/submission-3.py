class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n-1

        max_volume = 0

        while (l < r):
            volume = (r-l) * min(heights[l],heights[r])
            max_volume = max(max_volume, volume)

            if (heights[l] < heights[r]):
                l += 1
            else:
                r -= 1

        return max_volume
        