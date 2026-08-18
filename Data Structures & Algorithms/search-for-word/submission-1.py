class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        exists = False

        def dfs(row, col, i):
            nonlocal exists
            if (i == len(word)):
                exists = True
                return

            if (row < 0 or row == len(board) or col < 0 or col == len(board[0])):
                return

            if (board[row][col] == word[i]):
                temp = board[row][col]
                board[row][col] = "#"

                dfs(row+1, col, i+1)
                dfs(row, col+1, i+1)
                dfs(row-1, col, i+1)
                dfs(row, col-1, i+1)

                board[row][col] = temp

        for row in range (len(board)):
            for col in range (len(board[0])):
                dfs(row, col, 0)

        return exists



        
        