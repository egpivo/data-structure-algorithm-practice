from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(m \times n)
    - SC: O(1)
    """

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        perimeter = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    for dx, dy in directions:
                        new_row, new_col = row + dx, col + dy
                        if (
                            not (0 <= new_row < m and 0 <= new_col < n)
                            or grid[new_row][new_col] == 0
                        ):
                            perimeter += 1
        return perimeter


if __name__ == "__main__":
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    print(f"Solution: {Solution().islandPerimeter(grid)}")
