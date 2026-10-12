class Solution:
    def climbStairs(self, n: int) -> int:
        prev2 = 0
        prev1 = 1
        curr = 1

        for i in range(2, n + 1):
            prev2, prev1 = prev1, curr
            curr = prev2 + prev1

        return curr