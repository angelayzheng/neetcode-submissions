class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.charMap(s) == self.charMap(t)

    def charMap(self, s: str) -> dict[str, int]:
        chars = {}

        for c in s:
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1

        return chars