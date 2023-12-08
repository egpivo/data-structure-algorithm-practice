from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """ "
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
                    if (
                        0 <= nr < n
                        and 0 <= nc < n
                        and (nr, nc) not in seen
                        and grid[nr][nc] == 1
                    ):
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


class SolutionComponentDFS:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """
        Idea
        ----
        - Reduce the complexity from the first solution by removing the process of repeatedly calculating the same size.

        Complexity
        ----------
        - TC: O(N^2)
        - SC: O(N^2)
        """
        self.grid = grid
        self.nrows = len(grid)
        self.ncols = len(grid[0])

        area = {}
        index = 2
        for row in range(self.nrows):
            for col in range(self.ncols):
                if self.grid[row][col] == 1:
                    area[index] = self.dfs(row, col, index)
                    index += 1

        answer = max(area.values() or [0])
        for row in range(self.nrows):
            for col in range(self.ncols):
                if self.grid[row][col] == 0:
                    seen_indices = {
                        self.grid[nr][nc]
                        for nr, nc in self.neighbors(row, col)
                        if self.grid[nr][nc] > 1
                    }
                    answer = max(answer, 1 + sum(area[i] for i in seen_indices))

        return answer

    def neighbors(self, row, col):
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            if 0 <= new_row < self.nrows and 0 <= new_col < self.ncols:
                yield new_row, new_col

    def dfs(self, row, col, index):
        area = 1
        self.grid[row][col] = index
        for nr, nc in self.neighbors(row, col):
            if self.grid[nr][nc] == 1:
                area += self.dfs(nr, nc, index)
        return area


if __name__ == "__main__":
    grid = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 1, 1, 0], [1, 1, 0, 1]]
    expected_answer = 9
    print(
        f"Solution: {Solution().largestIsland(grid)} || expected answer: {expected_answer}"
    )
    print(
        f"Component Solution: {SolutionComponentDFS().largestIsland(grid)} || expected answer: {expected_answer}"
    )
