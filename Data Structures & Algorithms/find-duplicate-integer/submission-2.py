class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = nums[0]
        f = nums[nums[0]]

        while nums[s] != nums[f]:
            s = nums[s]
            f = nums[nums[f]]

        s2 = 0
        while s != s2:
            s = nums[s]
            s2 = nums[s2]

        return s