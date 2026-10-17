class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False
            
            seen.add(n)
            
            total = 0

            while n:
                n, digit = divmod(n, 10)
                total += digit * digit

            n = total

        return True

    def sumSquares(self, n: int) -> int:
        total = 0

        while n:
            n, digit = divmod(n, 10)
            total += digit * digit

        return total