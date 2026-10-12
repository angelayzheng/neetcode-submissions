class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = len(nums) - 1

        while nums[i] != i + 1:
            nums[i], i = i + 1, nums[i] - 1

        return nums[i]