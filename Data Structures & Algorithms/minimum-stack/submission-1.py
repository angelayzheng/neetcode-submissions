class MinStack:

    stack: list[int]
    min_stack: list[int]
    min_val: int

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.min_stack) == 0:
            self.min_stack.append(0)
        
        elif val < self.stack[self.min_stack[-1]]:
            self.min_stack.append(len(self.stack) - 1)

    def pop(self) -> None:
        self.stack.pop()

        if self.min_stack[-1] == len(self.stack):
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.min_stack[-1]]
