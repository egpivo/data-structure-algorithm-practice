from collections import defaultdict
from functools import cache
from typing import List


class Solution:
    """
    Complexity
    ----------
    - Time: O(mn) - memoization helps to reduce the time as it doesn't visit the same cell twice.
    - Space: O(mn)  space required for recursive call stack and cache.
    """

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        nrows = len(matrix)
        ncols = len(matrix[0])

        @cache
        def dfs(row, col):
            answer = 1
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                new_r = row + dx
                new_c = col + dy
                if (
                    0 <= new_r < nrows
                    and 0 <= new_c < ncols
                    and matrix[new_r][new_c] > matrix[row][col]
                ):
                    answer = max(answer, dfs(new_r, new_c) + 1)

            return answer

        return max(dfs(r, c) for r in range(nrows) for c in range(ncols))


if __name__ == "__main__":
    matrix = matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    print(f"Solution: {Solution().longestIncreasingPath(matrix)}")
