from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(mn4^k)
    - SC: O(mn)
    """

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = ((-1, 0), (1, 0), (0, 1), (0, -1))

        def dfs(row, col, visited):
            if (
                not (0 <= row < m and 0 <= col < n)
                or grid[row][col] == 0
                or (row, col) in visited
            ):
                return 0

            visited.add((row, col))
            max_gold = 0
            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy
                max_gold = max(
                    max_gold, grid[row][col] + dfs(next_row, next_col, visited)
                )

            visited.remove((row, col))
            return max_gold

        max_gold = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] != 0:
                    max_gold = max(max_gold, dfs(row, col, set()))

        return max_gold


if __name__ == "__main__":
    grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
    print(f"The solution is {Solution().getMaximumGold(grid)}")
