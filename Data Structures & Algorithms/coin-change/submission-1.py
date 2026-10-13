class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = [-1] * (amount+1)
        min_coins[0] = 0

        for i in range(1, amount + 1):
            for d in coins:
                if (i - d) >= 0 and min_coins[i - d] >= 0:
                    if min_coins[i] == -1:
                        min_coins[i] = min_coins[i - d] + 1
                    
                    elif min_coins[i - d] + 1 < min_coins[i]:
                        min_coins[i] = min_coins[i - d] + 1

        return min_coins[-1]
