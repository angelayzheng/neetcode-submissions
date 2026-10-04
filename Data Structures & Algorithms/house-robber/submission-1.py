class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        max1 = nums[0]
        max2 = max(nums[0], nums[1])

        for n in nums[2:]:
            max1, max2 = max2, max(max1 + n, max2)

        return max2
