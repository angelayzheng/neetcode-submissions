class PrefixTree:
    root: str
    subtrees: List[PrefixTree]
    end: bool

    def __init__(self):
        self.root = ""
        self.subtrees = [None] * 26
        self.end = False

    def insert(self, word: str) -> None:
        if len(word) == 0:
            return

        c = ord(word[0]) - ord('a')

        if not self.subtrees[c]:
            self.subtrees[c] = PrefixTree()
            self.subtrees[c].root = c

        if len(word) == 1:
            self.subtrees[c].end = True

        self.subtrees[c].insert(word[1:])

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return True

        if len(word) == 1:
            c = ord(word) - ord('a')
            
            if self.subtrees[c]:
                return self.subtrees[c].end

        c = ord(word[0]) - ord('a')
        if not self.subtrees[c]:
            return False

        return self.subtrees[c].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            return True

        c = ord(prefix[0]) - ord('a')

        if len(prefix) == 1 and self.subtrees[c]:
            return True

        if not self.subtrees[c]:
            return False

        return self.subtrees[c].startsWith(prefix[1:])
        
        