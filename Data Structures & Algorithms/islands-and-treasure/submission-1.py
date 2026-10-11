from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    queue.append(((i, j), 0))

        while len(queue) > 0:
            (i, j), dist = queue.popleft()

            if grid[i][j] == 2147483647 or grid[i][j] == 0:
                grid[i][j] = dist

                # up
                if self.validCoord(grid, i - 1, j) and grid[i - 1][j] == 2147483647:
                    queue.append(((i - 1, j), dist + 1))

                # down
                if self.validCoord(grid, i + 1, j) and grid[i + 1][j] == 2147483647:
                    queue.append(((i + 1, j), dist + 1))

                # left
                if self.validCoord(grid, i, j - 1) and grid[i][j - 1] == 2147483647:
                    queue.append(((i, j - 1), dist + 1))

                # right
                if self.validCoord(grid, i, j + 1) and grid[i][j + 1] == 2147483647:
                    queue.append(((i, j + 1), dist + 1))

    def validCoord(self, grid: List[List[int]], i: int, j: int) -> bool:
        return (0 <= i < len(grid)) and (0 <= j < len(grid[i]))
        
