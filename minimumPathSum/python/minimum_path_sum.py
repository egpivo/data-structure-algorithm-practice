import copy
from typing import List


class SolutionBruteForce:
    """
    Note
    ----
    - cost(i, j) = grid[i][j] + min(grid[i+1][j], grid[i][j+1])

    Complexity
    ----------
    - m: # rows
    - n: # colmns
    - TC: O(2^{m+n})
    - SC: O(m + n) (recursive depth)
    """

    def minPathSum(self, grid: List[List[int]]) -> int:
        return self.calculate(grid, 0, 0)

    def calculate(self, grid, row, col):
        if row == len(grid) or col == len(grid[0]):
            return float('inf')

        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            return grid[row][col]

        return grid[row][col] + min(self.calculate(grid, row + 1, col), self.calculate(grid, row, col + 1))


class SolutionDPI:
    """

    Complexity
    ----------
    - m: # rows
    - n: # colmns
    - TC: O(mn)
    - SC: O(1)
    """

    def minPathSum(self, grid: List[List[int]]) -> int:
        nrows = len(grid)
        ncols = len(grid[0])

        dp = [[0] * ncols for _ in range(nrows)]
        dp[0][0] = grid[0][0]

        for row in range(1, nrows):
            dp[row][0] = dp[row - 1][0] + grid[row][0]
        for col in range(1, ncols):
            dp[0][col] = dp[0][col - 1] + grid[0][col]

        for row in range(1, nrows):
            for col in range(1, ncols):
                dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + grid[row][col]
        return dp[nrows - 1][ncols - 1]


class SolutionDPII:
    """

    Complexity
    ----------
    - m: # rows
    - n: # colmns
    - TC: O(mn)
    - SC: O(1)
    """

    def minPathSum(self, grid: List[List[int]]) -> int:
        nrows = len(grid)
        ncols = len(grid[0])

        directions = ((-1, 0), (0, -1))

        for row in range(nrows):
            for col in range(ncols):
                updates = []
                for dx, dy in directions:
                    new_row, new_col = row + dx, col + dy
                    if 0 <= new_row < nrows and 0 <= new_col < ncols:
                        updates.append(grid[new_row][new_col])
                grid[row][col] += min(updates) if updates else 0

        return grid[nrows - 1][ncols - 1]


class SolutionDPIII:
    """

    Complexity
    ----------
    - m: # rows
    - n: # colmns
    - TC: O(mn)
    - SC: O(n)
    """

    def minPathSum(self, grid: List[List[int]]) -> int:
        nrows = len(grid)
        ncols = len(grid[0])

        dp = [0] * ncols

        for row in range(nrows - 1, -1, -1):
            for col in range(ncols - 1, -1, -1):
                if row != nrows - 1 and col == ncols - 1:
                    dp[col] += grid[row][col]
                elif row == nrows - 1 and col != ncols - 1:
                    dp[col] = grid[row][col] + dp[col + 1]
                elif row != nrows - 1 and col != ncols - 1:
                    dp[col] = grid[row][col] + min(dp[col], dp[col + 1])
                else:
                    dp[col] = grid[row][col]
        return dp[0]


if __name__ == "__main__":
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(f"{SolutionBruteForce().minPathSum(grid)}")
    print(f"{SolutionDPI().minPathSum(grid)}")
    print(f"{SolutionDPII().minPathSum(copy.deepcopy(grid))}")
    print(f"{SolutionDPIII().minPathSum(grid)}")
