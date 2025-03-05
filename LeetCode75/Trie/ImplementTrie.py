class Trie:

    def __init__(self):
        self._dict = {}
        self._is_end = False

    def insert(self, word: str) -> None:
        if len(word) == 0:
            self._is_end = True
            return
        if word[0] not in self._dict:
            self._dict[word[0]] = Trie()
        self._dict[word[0]].insert(word[1:])

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return self._is_end
        elif word[0] not in self._dict:
            return False
        return self._dict[word[0]].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            return True
        elif prefix[0] not in self._dict:
            return False
        return self._dict[prefix[0]].startsWith(prefix[1:])
