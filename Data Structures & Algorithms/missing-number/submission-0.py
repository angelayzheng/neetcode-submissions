class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1 = 0
        for n in nums:
            sum1 ^= n

        sum2 = 0
        for i in range(0, len(nums) + 1):
            sum2 ^= i

        return sum1 ^ sum2