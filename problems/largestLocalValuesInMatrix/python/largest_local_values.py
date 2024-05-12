from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n^2)
    - TC: O(n^2)
    """

    WINDOW_SIZE = 3

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        result_size = n - 2
        result = [[None] * result_size for _ in range(result_size)]

        # Precompute maximum values for each window row
        max_vals = [
            [
                max(row[i : i + self.WINDOW_SIZE])
                for i in range(n - self.WINDOW_SIZE + 1)
            ]
            for row in grid
        ]

        for row in range(result_size):
            for col in range(result_size):
                result[row][col] = max(
                    max_vals[row + i][col] for i in range(self.WINDOW_SIZE)
                )
        return result


if __name__ == "__main__":
    grid = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
    print(f"The solution is {Solution().largestLocal(grid)}")
