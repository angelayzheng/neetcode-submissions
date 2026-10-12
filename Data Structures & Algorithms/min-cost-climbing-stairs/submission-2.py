class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        min_cost2 = 0
        min_cost1 = 0
        min_cost0 = 0

        for i in range(2, n + 1):
            min_cost2, min_cost1 = min_cost1, min_cost0
            min_cost0 = min(min_cost2 + cost[i - 2], min_cost1 + cost[i - 1])

        return min_cost0
