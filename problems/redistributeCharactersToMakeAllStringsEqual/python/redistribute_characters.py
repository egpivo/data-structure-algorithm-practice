from collections import Counter
from typing import List


class Solution:
    """
    Complexity
    ----------
    - Time complexity: $O(m + n)$
        -  $m$ is the total number of characters in all the words
        -  $n$ is the number of words.
        - Counting the occurrences of characters using `Counter("".join(words))` takes $O(m)$ time.
        - Checking if each count is divisible by the number of words using `all(...)` takes $O(n)$ time.
    - Space complexity: $O(m)$
        - determined by the storage needed for the counts of characters, which is proportional to the total number of characters in all words.
    """

    def makeEqual(self, words: List[str]) -> bool:
        return all(
            count % len(words) == 0 for count in Counter("".join(words)).values()
        )


if __name__ == "__main__":
    words = ["abc", "aabc", "bc"]
    answer = Solution().makeEqual(words)
    print(answer)
