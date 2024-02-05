from collections import Counter


class Solution:
    """
    Complexity
    ----------
    - TC: O(length of `s`)
    - SC: O(# of distinct characters)
    """

    def firstUniqChar(self, s: str) -> int:
        char_count = Counter(s)
        for index, char in enumerate(s):
            if char_count[char] == 1:
                return index
        return -1


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    print(f"Solution: {Solution().firstUniqChar(s)}")
