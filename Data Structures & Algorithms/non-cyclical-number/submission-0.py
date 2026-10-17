class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            seen.add(n)
            n = self.sumSquares(n)

            if n == 1:
                return True

        return False

    def sumSquares(self, n: int) -> int:
        total = 0

        while n:
            n, digit = divmod(n, 10)
            total += digit * digit
            
        return total