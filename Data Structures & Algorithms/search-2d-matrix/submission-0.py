class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.rowSearch(matrix, target, 0, len(matrix))

        return self.binarySearch(matrix[row], target, 0, len(matrix[row]))

    def rowSearch(self, matrix: List[List[int]], target: int, b: int, e: int) -> int:

        if e - b <= 1:
            return b

        m = (b + e) // 2

        if target < matrix[m][0]:
            return self.rowSearch(matrix, target, b, m)

        else:
            return self.rowSearch(matrix, target, m, e)

    def binarySearch(self, row: List[int], target: int, b: int, e: int) -> bool:
        if b >= e:
            return False

        m = (b + e) // 2

        if target == row[m]:
            return True
        elif target < row[m]:
            return self.binarySearch(row, target, b, m)
        else:
            return self.binarySearch(row, target, m + 1, e)
