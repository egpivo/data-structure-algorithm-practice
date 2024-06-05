from collections import Counter
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC:
    - SC:
    """

    def commonChars(self, words: List[str]) -> List[str]:
        char_freq = Counter(words[0])

        for word in words[1:]:
            char_freq &= Counter(word)

        return list(char_freq.elements())


if __name__ == "__main__":
    words = ["bella", "label", "roller"]

    print(f"The solution is {Solution().commonChars(words)}")
