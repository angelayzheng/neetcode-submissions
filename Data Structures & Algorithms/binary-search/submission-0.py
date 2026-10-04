class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums))
    
    def binary_search(self, nums: List[int], target: int, b: int, e: int) -> int:
        if b >= e:
            return -1
            
        m = (b + e) // 2

        if target == nums[m]:
            return m
        elif target < nums[m]:
            return self.binary_search(nums, target, b, m)
        else:
            return self.binary_search(nums, target, m + 1, e)
