from collections import Counter
from typing import List


class Solution:
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


if __name__ == "__main__":
    arr = [4, 3, 1, 1, 3, 3, 2]
    k = 3
    print(f"Solution: {Solution().findLeastNumOfUniqueInts(arr, k)}")
