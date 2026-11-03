class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        right_boundaries = [n-1] * n

        monotonic_stack = []
        monotonic_stack.append(0)

        for i in range(1, n):
            curr = heights[i]
            while monotonic_stack and curr < heights[monotonic_stack[-1]]:
                right_boundaries[monotonic_stack[-1]] = i - 1
                monotonic_stack.pop()

            monotonic_stack.append(i)

        left_boundaries = [0] * n
        monotonic_stack.clear()
        monotonic_stack.append(n-1)

        for i in range(n-2, -1, -1):
            curr = heights[i]
            while monotonic_stack and curr < heights[monotonic_stack[-1]]:
                left_boundaries[monotonic_stack[-1]] = i + 1
                monotonic_stack.pop()

            monotonic_stack.append(i)

        max_area = 0

        for i in range(n):
            area = heights[i] * (right_boundaries[i] - left_boundaries[i] + 1)
            max_area = max(area, max_area)

        return max_area

