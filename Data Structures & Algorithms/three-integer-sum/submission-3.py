class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []

        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] > 0:
                break

            result.extend(self.twoSum(nums, -nums[i], i + 1))

        return result

    def twoSum(self, nums: List[int], target: int, start: int) -> List[List[int]]:
        result = []
        
        j = start
        k = len(nums) - 1

        while j < k:
            if nums[j] + nums[k] == target:
                result.append([-target, nums[j], nums[k]])
                j += 1
                k -= 1
                
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1

            elif nums[j] + nums[k] < target:
                j += 1

                while nums[j - 1] == nums[j] and j < k:
                    j += 1

            else:
                k -= 1

                while nums[k] == nums[k + 1] and j < k:
                    k -= 1

        return result
