from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self._get_node(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        return self._get_node(prefix) is not None

    def _get_node(self, prefix: str) -> TrieNode:
        current = self.root
        for char in prefix:
            current = current.children.get(char)
            if not current:
                return None
        return current
