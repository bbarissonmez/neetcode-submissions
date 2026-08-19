class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for _ in range (len(grid[0]))] for _ in range(len(grid))]
        count = 0
        
        def dfs(row, col):
            nonlocal count, visited
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return

            if (grid[row][col] == '1'):
                if visited[row][col]:
                    return
                else:
                    visited[row][col] = True
            else:
                return


            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if not visited[row][col] and grid[row][col] == '1':
                    dfs(row, col)
                    count += 1
                
        return count