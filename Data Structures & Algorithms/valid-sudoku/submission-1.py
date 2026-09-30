class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        for row in board:
            vals = set()
            for cell in row:
                if not cell == "." and cell in vals:
                    return False
                vals.add(cell)

        # cols
        for i in range(len(board)):
            vals = set()
            for j in range(len(board)):
                cell = board[j][i]
                if not cell == "." and cell in vals:
                    return False
                vals.add(cell)

        # squares
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                vals = set()
                for r in range(0, 3):
                    for c in range(0, 3):
                        if not board[i + r][j + c] == "." and board[i + r][j + c] in vals:
                            return False
                        vals.add(board[i + r][j + c])

        return True
