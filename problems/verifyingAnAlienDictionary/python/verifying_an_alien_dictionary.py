from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        """
        Complexity
        ----------
        - M: # of characters in words
        TC: O(M)
        SC: O(1)
        """
        order_map = {char: idx for idx, char in enumerate(order)}

        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return False

                if order_map[words[i][j]] != order_map[words[i + 1][j]]:
                    if order_map[words[i][j]] > order_map[words[i + 1][j]]:
                        return False
                    break
        return True


if __name__ == "__main__":
    words = ["hello", "leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    print(f"Solution: {Solution().isAlienSorted(words, order)}")

    words = ["apple", "app"]
    order = "abcdefghijklmnopqrstuvwxyz"
    print(f"Solution: {Solution().isAlienSorted(words, order)}")
