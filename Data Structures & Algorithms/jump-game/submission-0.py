class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = nums[0]

        for n in nums[1:]:
            gas -= 1
            if gas < 0:
                return False
            if n > gas:
                gas = n

        return True