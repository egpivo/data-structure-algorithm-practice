class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        anchor = word.index(ch) + 1
        return word[:anchor][::-1] + word[anchor:]


if __name__ == "__main__":
    word = "abcdefd"
    ch = "d"
    print(f"Solution: {Solution().reversePrefix(word, ch)}")
