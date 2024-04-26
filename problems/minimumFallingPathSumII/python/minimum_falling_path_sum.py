import heapq
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n^2 \log n)
    - SC: O(1)
    """

    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return grid[0][0]

        for row in range(1, n):
            min_val, next_min_val = heapq.nsmallest(2, grid[row - 1])
            grid[row] = [
                cell + (next_min_val if prev == min_val else min_val)
                for prev, cell in zip(grid[row - 1], grid[row])
            ]
        return min(grid[-1])


if __name__ == "__main__":
    matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
    print(f"{Solution().minFallingPathSum(matrix)}")
