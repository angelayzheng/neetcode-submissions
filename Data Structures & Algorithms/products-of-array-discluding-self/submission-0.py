class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1] * len(nums)
        prod = 1

        for i in range(len(nums)):
            arr[i] = prod
            prod *= nums[i]

        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            arr[i] *= prod
            prod *= nums[i]

        return arr