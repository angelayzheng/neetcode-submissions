class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        nums.sort()

        max_seq = 1
        seq = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue

            elif nums[i] == nums[i - 1] + 1:
                seq += 1

            else:
                if seq > max_seq:
                    max_seq = seq

                seq = 1

        if seq > max_seq:
            max_seq = seq

        return max_seq