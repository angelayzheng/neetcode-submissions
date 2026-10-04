class Solution:
    def rob(self, nums: List[int]) -> int:
        max1 = 0
        max2 = 0

        for n in nums:
            max1, max2 = max2, max(max1 + n, max2)

        return max2
