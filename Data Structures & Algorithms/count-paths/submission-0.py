class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[None for _ in range(n)] for _ in range(m)]

        def dfs(row, col):

            if (row < 0 or row >= m or col < 0 or col >= n):
                return 0

            if (row == m - 1 and col == n - 1):
                return 1

            if (grid[row][col] == None):
                grid[row][col] = dfs(row+1, col) + dfs(row, col+1)

            return grid[row][col]

        return dfs(0,0)
            
        