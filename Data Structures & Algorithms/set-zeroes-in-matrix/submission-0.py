class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows = []
        cols = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)

        for r in rows:
            matrix[r] = [0] * len(matrix[0])

        for c in cols:
            for i in range(len(matrix)):
                matrix[i][c] = 0