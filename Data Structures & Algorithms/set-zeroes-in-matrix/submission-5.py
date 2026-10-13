class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        first_row = False

        # first row
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                first_row = True
                break

        # first column
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                matrix[0][0] = 0
                break

        # go through all to mark
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # mark the zeros in rows
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[0])):
                    matrix[i][j] = 0

        # mark the zeros in cols
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(1, len(matrix)):
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(1, len(matrix)):
                matrix[i][0] = 0

        if first_row:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
