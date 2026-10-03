class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for n in tokens:
            if n in {"+", "-", "*", "/"}:
                n2 = stack.pop()
                n1 = stack.pop()
                
            if n == "+":
                stack.append(n1 + n2)
            elif n == "-":
                stack.append(n1 - n2)
            elif n == "*":
                stack.append(n1 * n2)
            elif n == "/":
                stack.append(int(n1 / n2))
            else:
                stack.append(int(n))            

        return stack[0]