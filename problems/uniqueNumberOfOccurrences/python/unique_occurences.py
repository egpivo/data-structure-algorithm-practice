from collections import Counter
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        frequency_counts = Counter(arr)
        return len(set(frequency_counts.values())) == len(frequency_counts)


if __name__ == "__main__":
    arr = [1, 2, 2, 1, 1, 3]
    print(f"{Solution().uniqueOccurrences(arr)}")
