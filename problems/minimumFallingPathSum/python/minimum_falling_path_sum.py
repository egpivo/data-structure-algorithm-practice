from typing import List


class SolutionDFS:
    """
    Complexity
    ----------
    - TC: O(n^3)
    - SC: O(n^2)
    """

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        directions = ((1, -1), (1, 0), (1, 1))
        visited = {}

        def dfs(row, col):
            if row == n - 1:
                return matrix[row][col]

            if (row, col) in visited:
                return visited[(row, col)]

            min_value = float("inf")
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < n and 0 <= new_col < n:
                    min_value = min(min_value, matrix[row][col] + dfs(new_row, new_col))

            visited[(row, col)] = min_value
            return min_value

        min_sum = float("inf")
        for col in range(n):
            path_sum = dfs(0, col)
            min_sum = min(min_sum, path_sum)

        return min_sum


class SolutionDP:
    """
    Complexity
    ----------
    - TC: O(n^2)
    - SC: O(n^2)
    """

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        n = len(matrix)
        dp = [[0] * n for _ in range(n)]
        dp[-1] = matrix[-1][:]

        for i in range(n - 2, -1, -1):
            for j in range(n):
                dp[i][j] = matrix[i][j] + min(
                    dp[i + 1][max(j - 1, 0)], dp[i + 1][j], dp[i + 1][min(j + 1, n - 1)]
                )

        return min(dp[0])


if __name__ == "__main__":
    matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
    print(f"{SolutionDFS().minFallingPathSum(matrix)}")
    print(f"{SolutionDP().minFallingPathSum(matrix)}")
