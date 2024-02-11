from itertools import product
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(m * n^2)
    - SC: O(m * n^2)
    """

    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = {}  # To store results of subproblems
        col_directions = (-1, 0, 1)  # Possible column directions to move

        def dfs(row, col1, col2):
            # Base case: if either cherry picker goes out of bounds, return negative infinity
            if not (0 <= col1 < n and 0 <= col2 < n):
                return float("-inf")

            # Check if result for this state is already computed
            if (row, col1, col2) in visited:
                return visited[(row, col1, col2)]

            # Cherry count for the current cell(s)
            result = grid[row][col1] + (grid[row][col2] if col1 != col2 else 0)

            # If not at the bottom row, explore all valid next states and get the max cherries
            if row < m - 1:
                max_cherries = max(
                    dfs(row + 1, col1 + dy1, col2 + dy2)
                    for dy1, dy2 in product(col_directions, repeat=2)
                )
                result += max_cherries

            # Memoize the result for this state
            visited[(row, col1, col2)] = result
            return result

        # Start the recursion from the top row with cherry pickers at the two ends
        return dfs(0, 0, n - 1)


if __name__ == "__main__":
    grid = [[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]
    print(f"The answer is {Solution().cherryPickup(grid)}")
