class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets, col_sets, box_sets = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]

        for i in range (9):
            for j in range(9):
                num = board[i][j]
                if (num == "."):
                    continue

                if num in row_sets[i]:
                    return False
                else:
                    row_sets[i].add(num)

                if num in col_sets[j]:
                    return False
                else:
                    col_sets[j].add(num)

                if num in box_sets[(i // 3) * 3 + (j // 3)]:
                    return False
                else:
                    box_sets[(i//3) * 3 + (j//3)].add(num)

        return True