class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if self.isOpen(c):
                stack.append(c)
            elif len(stack) == 0 or not self.bracketMatches(stack.pop(), c):
                return False

        return len(stack) == 0

    def isOpen(self, s: str) -> bool:
        return s in {"(", "[", "{"}

    def bracketMatches(self, s1: str, s2: str) -> bool:
        return (s1, s2) in {("[", "]"), ("{", "}"), ("(", ")")}