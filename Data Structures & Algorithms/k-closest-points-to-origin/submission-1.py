import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for (xi, yi) in points:
            dist = math.sqrt(xi ** 2 + yi ** 2)
            heapq.heappush(heap, (-dist, xi, yi))

            if len(heap) > k:
                heapq.heappop(heap)

        return [[v[1], v[2]] for v in heap]
