class PrefixTree:
    root: str
    subtrees: dict[str, PrefixTree]
    end: bool

    def __init__(self):
        self.root = ""
        self.subtrees = {}
        self.end = False

    def insert(self, word: str) -> None:
        if len(word) == 0:
            return

        c = word[0]

        if c not in self.subtrees:
            self.subtrees[c] = PrefixTree()
            self.subtrees[c].root = c

        if len(word) == 1:
            self.subtrees[c].end = True

        self.subtrees[c].insert(word[1:])

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return True

        if len(word) == 1 and word in self.subtrees:
            return self.subtrees[word].end

        c = word[0]
        if c not in self.subtrees:
            return False

        return self.subtrees[c].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            return True

        if len(prefix) == 1 and prefix in self.subtrees:
            return True

        c = prefix[0]
        if c not in self.subtrees:
            return False

        return self.subtrees[c].startsWith(prefix[1:])
        
        