import random
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC:
        - constructor: O(N)
        - `pirckIndex`: O(N)
    - SC:
        - constructor: O(N)
        - `pickIndex`: O(1)
    """

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        target = self.total_sum * random.random()
        for idx, prefix_sum in enumerate(self.prefix_sums):
            if target < prefix_sum:
                return idx

class SolutionBS:
    """
    Complexity
    ----------
    - TC:
        - constructor: O(N)
        - `pirckIndex`: O(logN)
    - SC:
        - constructor: O(N)
        - `pickIndex`: O(1)
    """
    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        target = self.total_sum * random.random()
        low = 0
        high = len(self.prefix_sums)
        while low < high:
            mid = low + (high - low) // 2
            if target > self.prefix_sums[mid]:
                low = mid + 1
            else:
                high = mid

        return low
if __name__ == "__main__":
    w = [1, 3, 2, 5]
    obj = Solution(w)
    print(f"Random pick: {Solution(w).pickIndex()}")
    print(f"Random pick: {SolutionBS(w).pickIndex()}")
