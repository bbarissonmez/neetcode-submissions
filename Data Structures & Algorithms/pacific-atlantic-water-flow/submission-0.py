class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW_LEN = len(heights)
        COL_LEN = len(heights[0])

        atlantic = set()
        pacific = set()

        directions = [[0,1], [1,0], [-1,0], [0, -1]]

        border_indices_pacific = list({(r,c) for r in range(ROW_LEN) for c  in range(COL_LEN) if r == 0 or c == 0})
        border_indices_atlantic = list({(r,c) for r in range(ROW_LEN) for c  in range(COL_LEN) if r == ROW_LEN-1 or c == COL_LEN-1})

        def dfs_pacific(row, col, invader):
            if row < 0 or row >= ROW_LEN or col < 0 or col >= COL_LEN:
                return

            if heights[row][col] >= invader and (row,col) not in pacific:
                pacific.add((row, col))
                for (h,v) in directions:
                    dfs_pacific(row+h, col+v, heights[row][col])

        def dfs_atlantic(row, col, invader):
            if row < 0 or row >= ROW_LEN or col < 0 or col >= COL_LEN:
                return

            if heights[row][col] >= invader and (row,col) not in atlantic:
                atlantic.add((row, col))
                for (h,v) in directions:
                    dfs_atlantic(row+h, col+v, heights[row][col])

        for r,c in border_indices_pacific:
            dfs_pacific(r,c, heights[r][c])

        for r,c in border_indices_atlantic:
            dfs_atlantic(r,c, heights[r][c])

        return list(atlantic.intersection(pacific))
        