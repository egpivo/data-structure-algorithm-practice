from collections import Counter
from typing import List


class Solution1:
    """
    Complexity
    ----------
    - TC: O(n\log(n))
    - SC: O(n)
    """

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        unique_count = len(freq)

        for _, count in reversed(freq.most_common()):
            if k >= count:
                k -= count
                unique_count -= 1
            else:
                break

        return unique_count


class Solution2:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freqs = Counter(arr)
        unique_count = len(freqs)
        historgram = Counter(freqs.values())

        for freq in range(1, len(arr) + 1):
            if k >= freq * historgram[freq]:
                k -= freq * historgram[freq]
                unique_count -= historgram[freq]
            else:
                break

        return unique_count - k // freq


if __name__ == "__main__":
    arr = [2, 4, 1, 8, 3, 5, 1, 3]
    k = 3
    print(f"Solution: {Solution1().findLeastNumOfUniqueInts(arr, k)}")
    print(f"Solution: {Solution2().findLeastNumOfUniqueInts(arr, k)}")
