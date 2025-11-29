from collections import deque
from typing import List


class SolutionDFS:
    """
    Complexity
    ----------
    - TC: O(mn)
    - SC: O(mn)
    """

    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def colorBorder(
        self, grid: List[List[int]], row: int, col: int, color: int
    ) -> List[List[int]]:
        nrows = len(grid)
        ncols = len(grid[0])

        seen = set()
        border = set()

        def dfs(x, y, color):
            if (x, y) in seen:
                return

            seen.add((x, y))
            is_on_border = False
            for dx, dy in self.directions:
                new_x, new_y = x + dx, y + dy
                if (
                    0 <= new_x < nrows
                    and 0 <= new_y < ncols
                    and grid[new_x][new_y] == color
                ):
                    dfs(new_x, new_y, color)
                else:
                    is_on_border = True

            if is_on_border:
                border.add((x, y))

        dfs(row, col, grid[row][col])
        for x, y in border:
            grid[x][y] = color

        return grid


class SolutionBFS:
    """
    Complexity
    ----------
    - TC: O(mn)
    - SC: O(mn)
    """

    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def colorBorder(
        self, grid: List[List[int]], row: int, col: int, color: int
    ) -> List[List[int]]:
        nrows = len(grid)
        ncols = len(grid[0])
        queue = deque([(row, col)])

        seen = set()
        border = set()

        while queue:
            x, y = queue.popleft()

            if (x, y) in seen:
                continue

            seen.add((x, y))
            for dx, dy in self.directions:
                new_x, new_y = x + dx, y + dy
                if not (
                    0 <= new_x < nrows
                    and 0 <= new_y < ncols
                    and grid[new_x][new_y] == grid[x][y]
                ):
                    border.add((x, y))
                    continue
                if (new_x, new_y) not in queue:
                    queue.append((new_x, new_y))

        for x, y in border:
            grid[x][y] = color
        return grid


if __name__ == "__main__":
    grid = [[1, 2, 2], [2, 3, 2]]
    row = 0
    col = 1
    color = 3
    print(f"Solution: {SolutionDFS().colorBorder(grid, row, col, color)}")
    print(f"Solution: {SolutionBFS().colorBorder(grid, row, col, color)}")
