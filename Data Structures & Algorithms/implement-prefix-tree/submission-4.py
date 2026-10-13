class PrefixTree:
    subtrees: List[PrefixTree]
    end: bool

    def __init__(self):
        self.subtrees = [None] * 26
        self.end = False

    def insert(self, word: str) -> None:
        curr = self

        for c in word:
            i = ord(c) - ord('a')

            if not curr.subtrees[i]:
                curr.subtrees[i] = PrefixTree()
            
            curr = curr.subtrees[i]
            
        curr.end = True

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return True

        curr = self

        for c in word:
            i = ord(c) - ord('a')

            if not curr.subtrees[i]:
                return False

            curr = curr.subtrees[i]

        return curr.end

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            return True

        curr = self

        for c in prefix:
            i = ord(c) - ord('a')

            if not curr.subtrees[i]:
                return False

            curr = curr.subtrees[i]

        return True
        