from collections import defaultdict
from typing import Optional


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False


class Trie:
    """
    Complexity
    ----------
    - Time complexity:
        - Trie Insertion: $O(m)$, where $m$ is the length of the word being inserted.
        - Trie Search: $O(m)$, where $m$ is the length of the word being searched.
        - Trie Prefix Search: $O(m)$, where $m$ is the length of the prefix being searched.
    - Space complexity:
        - Trie Insertion: $O(m)$, where $m$ is the length of the word being inserted.
        - Trie Search: $O(1)$
        - Trie Prefix Search: $O(1)$
    """

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

    def _get_node(self, prefix: str) -> Optional[TrieNode]:
        current = self.root
        for char in prefix:
            current = current.children.get(char)
            if not current:
                return None
        return current
