class Solution:
    def trap(self, height: List[int]) -> int:
        lefts = []
        rights = []

        max_left = 0
        max_right = 0

        for i in range (len(height)):
            lefts.append(max_left)
            max_left = max(height[i], max_left)

        for j in range (len(height)-1, -1, -1):
            rights.append(max_right)
            max_right = max(height[j], max_right)

        rights.reverse()
        sum = 0
        for i in range(len(height)):
            if min(lefts[i], rights[i]) - height[i] < 0:
                continue
            sum += min(lefts[i], rights[i]) - height[i]
        return sum
        