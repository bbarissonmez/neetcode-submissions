class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_length = len(matrix)
        col_length = len(matrix[0])

        seen = set()

        for i in range (row_length):
            for j in range (col_length): 
                if matrix[i][j] == 0:
                    seen.add((i,j))

        for (i, j) in seen:
            for row in range(row_length):
                matrix[row][j] = 0

            for col in range(col_length):
                matrix[i][col] = 0

        

