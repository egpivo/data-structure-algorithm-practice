from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word


class Solution:
    """
    Complexity
    ----------
    Time complexity: $O(n \cdot m \cdot 4^L)$
    Space complexity: $O(W \cdot L)$
    - $W$: the number of words
    - $n \cdot m$: the size of `board`
    - $L$ is the average length of the `words`.
    """

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n, m = len(board), len(board[0])

        # Build trie from the given words
        trie = Trie()
        for word in words:
            trie.insert(word)
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def backtrack(row, col, node):
            char = board[row][col]
            if char not in node.children:
                return

            next_node = node.children[char]
            if next_node.word:
                result.append(next_node.word)
                next_node.word = None  # Avoid duplicate word

            board[row][col] = "visited"  # Mark as visited
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < n and 0 <= new_col < m:
                    backtrack(new_row, new_col, next_node)
            board[row][col] = char  # Restore the cell value

        result = []

        for row in range(n):
            for col in range(m):
                backtrack(row, col, trie.root)

        return result


if __name__ == "__main__":
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    words = ["oath", "pea", "eat", "rain"]
    print(f"{Solution().findWords(board, words)}")
