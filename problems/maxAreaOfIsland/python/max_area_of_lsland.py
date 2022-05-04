from typing import List


class SolutionDFS:
    """
    Complexity
    ----------
    - TC: O(mn)
    - SC: O(mn)
    """
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nrows = len(grid)
        ncols = len(grid[0])

        def dfs(row, col, index):
            if not (0 <= row < nrows and 0 <= col < ncols and grid[row][col] == 1):
                return 0
            area = 1
            grid[row][col] = index
            for dx, dy in self.directions:
                new_r, new_c = row + dx, col + dy
                area += dfs(new_r, new_c, index)

            return area

        max_area = 0
        index = 2
        for row in range(nrows):
            for col in range(ncols):
                if grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col, index + 1))
                    index += 1

        return max_area


if __name__ == "__main__":
    grids = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
             [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
             [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    print(f"Solution: {SolutionDFS().maxAreaOfIsland(grids)}")
