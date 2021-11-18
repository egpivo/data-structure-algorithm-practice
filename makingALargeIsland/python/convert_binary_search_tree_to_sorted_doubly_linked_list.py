from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """

        Idea
        ----
        - Find grid with zero --> dfs for 1's --> count the area

        Complexity
        ----------
        - TC: O(N^4)
        - SC: O(N^2)
        """
        n = len(grid)

        def dfs(row, col):
            seen = {(row, col)}
            stack = [(row, col)]

            while stack:
                r, c = stack.pop()
                for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                    if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in seen and grid[nr][nc] == 1:
                        stack.append((nr, nc))
                        seen.add((nr, nc))

            return len(seen)

        has_zero = False
        answer = 0
        for row, row_values in enumerate(grid):
            for col, value in enumerate(row_values):
                if value == 0:
                    has_zero = True
                    grid[row][col] = 1
                    answer = max(answer, dfs(row, col))
                    grid[row][col] = 0

        return answer if has_zero else n * n


if __name__ == "__main__":
    grid = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 1, 1, 0], [1, 1, 0, 1]]
    expected_answer = 9
    print(f"Solution: {Solution().largestIsland(grid)} || expected answer: {expected_answer}")
