from typing import List


class Solution:
    """

    Idea
    ----
    1. move all chips at odd positions to 1 at no cost
    2. move all chips at even positions to 0 at no cost.
    3  see whether we want to move all chips from 0 to 1 or from 1 to 0

    Complexity
    ----------
    - TC: O(n)
    - SC: O(1)
    """

    def minCostToMoveChips(self, position: List[int]) -> int:
        num_even = num_odd = 0

        for chip in position:
            if chip % 2 == 0:
                num_even += 1
            else:
                num_odd += 1
        return min(num_odd, num_even)


class Solution2:
    def minCostToMoveChips(self, position: List[int]) -> int:
        result = [chip % 2 for chip in position]
        return min(result.count(0), result.count(1))


class SolutionBitWise:
    def minCostToMoveChips(self, position: List[int]) -> int:
        d = [0, 0]
        for chip in position:
            d[chip & 1] += 1
        return min(d)


if __name__ == "__main__":
    position = [1, 2, 3]
    print(f"{Solution().minCostToMoveChips(position)}")
    print(f"{Solution2().minCostToMoveChips(position)}")
    print(f"{SolutionBitWise().minCostToMoveChips(position)}")
