class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        result = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            while len(stack) > 0:
                j = stack.pop()
                if temperatures[i] > temperatures[j]:
                    result[j] = i - j
                else:
                    stack.append(j)
                    break

            stack.append(i)

        return result
