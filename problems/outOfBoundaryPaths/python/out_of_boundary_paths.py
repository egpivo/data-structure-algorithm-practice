from collections import defaultdict


class Solution:
    """
    Complexity
    ----------
    - TC: O(n * m * maxMove)
    - SC: O(n * m * maxMove)
    """

    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        modulo = 10**9 + 7
        cache_path = defaultdict(int)

        def dfs(row, col, move):
            if move > maxMove:
                return 0
            if not 0 <= row < m or not 0 <= col < n:
                return 1

            if (row, col, move) in cache_path:
                return cache_path[(row, col, move)]

            result = 0
            for dx, dy in directions:
                result += dfs(row + dx, col + dy, move + 1)
                result %= modulo

            cache_path[(row, col, move)] = result
            return result

        return dfs(startRow, startColumn, 0)


if __name__ == "__main__":
    output = Solution().findPaths(1, 3, 3, 0, 1)
    assert output == 12, f"Wrong answer, but got {output}"
