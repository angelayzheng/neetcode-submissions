class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for l in range(len(prices) - 1):
            if prices[l + 1] <= prices[l]:
                continue

            for r in range(l + 1, len(prices)):
                if r < len(prices) - 1 and prices[r + 1] >= prices[r]:
                    continue

                else:
                    max_profit = max(max_profit, prices[r] - prices[l])

        return max_profit
