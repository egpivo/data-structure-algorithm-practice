from collections import defaultdict
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hash_map = defaultdict(int)
        count = 0
        for t in time:
            if t % 60 == 0:
                count += hash_map[0]
            else:
                count += hash_map[60 - t % 60]

            hash_map[t % 60] += 1

        return count


if __name__ == "__main__":
    time = [30, 20, 150, 100, 40, 60]
    print(f"{Solution().numPairsDivisibleBy60(time)}")
