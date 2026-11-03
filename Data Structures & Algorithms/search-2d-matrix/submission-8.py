import bisect

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m - 1

        while (l <= r):
            mid_row = l + (r - l) // 2

            if target >= matrix[mid_row][0] and target <= matrix[mid_row][-1]:
                break
            elif target < matrix[mid_row][0]:
                r = mid_row - 1
            else:
                l = mid_row + 1

        index = bisect.bisect_left(matrix[mid_row], target)

        if index < n and matrix[mid_row][index] == target:
            return True
        else:
            return False