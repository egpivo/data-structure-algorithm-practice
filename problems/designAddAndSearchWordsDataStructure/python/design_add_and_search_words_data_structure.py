from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False


class WordDictionary:
    """
    Complexity
    ----------
    - Time complexity:
       - $O(m)$, where $m$ is the length of the word being added.
       - $O(n \cdot m)$, where $n$ is the number of Trie nodes and $m$ is the length of the word being searched.
    - Space complexity:
       - $O(n \cdot m)$, where $n$ is the total number of Trie nodes and $m$ is the average length of the words.
    """

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        nodes = [self.root]
        for char in word:
            if char == ".":
                nodes = [child for node in nodes for child in node.children.values()]
            else:
                nodes = [
                    node.children.get(char) for node in nodes if char in node.children
                ]
        return any(node.is_end for node in nodes)
