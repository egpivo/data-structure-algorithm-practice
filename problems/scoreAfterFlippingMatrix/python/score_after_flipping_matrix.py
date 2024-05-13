from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Flip rows if necessary to maximize score
        for r in range(m):
            if grid[r][0] == 0:
                self.flip_row(grid, r)

        # Flip columns if necessary to maximize score
        for c in range(1, n):
            if sum(row[c] for row in grid) < len(grid) / 2:
                self.flip_col(grid, c)

        return self.calculate_score(grid)

    def flip_row(self, grid: List[List[int]], r: int) -> None:
        grid[r] = [1 - num for num in grid[r]]

    def flip_col(self, grid: List[List[int]], c: int) -> None:
        for row in grid:
            row[c] = 1 - row[c]

    def calculate_score(self, grid: List[List[int]]) -> int:
        total = 0
        for row in grid:
            total += sum(1 << i for i, num in enumerate(reversed(row)) if num)
        return total


if __name__ == "__main__":
    grid = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
    print(f"Solution: {Solution().matrixScore(grid)}")
