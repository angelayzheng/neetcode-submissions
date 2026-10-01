class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prev_i = -1001
        
        for i in range(len(numbers)):
            if numbers[i] == prev_i:
                continue

            diff = target - numbers[i]

            prev_j = -1001

            for j in range(i + 1, len(numbers)):

                if numbers[j] == diff:
                    return [i + 1, j + 1]
                elif numbers[j] > diff:
                    break

            prev_i = numbers[i]
