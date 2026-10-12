from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = [[False] * len(heights[0]) for _ in range(len(heights))]
        atlantic = [[False] * len(heights[0]) for _ in range(len(heights))]

        pacific_queue = deque()
        atlantic_queue = deque()

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Pacific

        # start at row 0
        for j in range(len(heights[0])):
            pacific[0][j] = True
            pacific_queue.append((0, j))
            
        # start at col 0
        for i in range(len(heights)):
            pacific[i][0] = True
            pacific_queue.append((i, 0))

        while len(pacific_queue) > 0:
            i, j = pacific_queue.popleft()

            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if 0 <= ni < len(heights) and 0 <= nj < len(heights[0]) and heights[i][j] <= heights[ni][nj] and not pacific[ni][nj]:
                    pacific[ni][nj] = True
                    pacific_queue.append((ni, nj))

        # Atlantic

        # start at last row
        for j in range(len(heights[-1])):
            atlantic[-1][j] = True
            atlantic_queue.append((len(heights) - 1, j))
            
        # start at last col
        for i in range(len(heights)):
            atlantic[i][-1] = True
            atlantic_queue.append((i, len(heights[0]) - 1))

        while len(atlantic_queue) > 0:
            i, j = atlantic_queue.popleft()

            for di, dj in directions:
                ni = i + di
                nj = j + dj
                
                if 0 <= ni < len(heights) and 0 <= nj < len(heights[0]) and heights[i][j] <= heights[ni][nj] and not atlantic[ni][nj]:
                    atlantic[ni][nj] = True
                    atlantic_queue.append((ni, nj))       

        # Combine
        res = []

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])

        return res
            