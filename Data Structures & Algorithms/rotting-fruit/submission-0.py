from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = set()
        curr_queue = deque()
        next_queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    fresh.add((i, j))

                elif grid[i][j] == 2:
                    curr_queue.append(((i, j), (-1, 0)))
                    curr_queue.append(((i, j), (1, 0)))
                    curr_queue.append(((i, j), (0, -1)))
                    curr_queue.append(((i, j), (0, 1)))

        time = 0

        while len(fresh) > 0:
            if len(curr_queue) == 0:
                return -1

            time += 1

            while len(curr_queue) > 0:
                cr, dr = curr_queue.popleft()
                i = cr[0] + dr[0]
                j = cr[1] + dr[1]

                if (0 <= i < len(grid)) and (0 <= j < len(grid[i])) and  grid[i][j] == 1:
                    grid[i][j] = 2
                    fresh.remove((i, j))

                    next_queue.append(((i, j), (-1, 0)))
                    next_queue.append(((i, j), (1, 0)))
                    next_queue.append(((i, j), (0, -1)))
                    next_queue.append(((i, j), (0, 1)))

            curr_queue = next_queue
            next_queue = deque()

        return time
