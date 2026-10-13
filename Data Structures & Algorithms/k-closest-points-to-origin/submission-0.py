import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for (xi, yi) in points:
            dist = math.sqrt(xi ** 2 + yi ** 2)

            heapq.heappush(heap, (dist, xi, yi))

        res = []
        for _ in range(k):
            _, i, j = heapq.heappop(heap)
            res.append([i, j])

        return res
