class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [int(tokens[0])]

        for n in tokens[1:]:
            try:
                stack.append(int(n))
            
            except ValueError:
                n2 = stack.pop()
                n1 = stack.pop()

                if n == "+":
                    stack.append(n1 + n2)
                elif n == "-":
                    stack.append(n1 - n2)
                elif n == "*":
                    stack.append(n1 * n2)
                else:
                    stack.append(int(n1 / n2))

        return stack[0]