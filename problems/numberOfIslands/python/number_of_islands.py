import copy
from collections import deque
from typing import List


class UnionFind:
    def __init__(self, size, max_count):
        self.root = [i for i in range(size)]
        self.max_count = max_count

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            self.root[root_y] = root_x
            self.max_count -= 1


class SolutionUnionFind:
    def numIslands(self, grid: List[List[str]]) -> int:
        nrow = len(grid)
        ncol = len(grid[0])

        max_count = sum(grid[i][j] == "1" for i in range(nrow) for j in range(ncol))
        uf = UnionFind(nrow * ncol, max_count)

        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == "0":
                    continue
                index = i * ncol + j
                if j < ncol - 1 and grid[i][j + 1] == "1":
                    uf.union(index, index + 1)
                if i < nrow - 1 and grid[i + 1][j] == "1":
                    uf.union(index, index + ncol)

        return uf.max_count


class SolutionDFS:
    """
    Notes
    -----
    - TC: O(mn)
    - SC: O(mn)
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid), len(grid[0])

        def is_valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == "1"

        def dfs(row, col):
            if not is_valid(row, col):
                return 0
            grid[row][col] = "visited"
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if is_valid(new_row, new_col):
                    dfs(new_row, new_col)

            return 1

        return sum(
            dfs(row, col)
            for row in range(m)
            for col in range(n)
            if grid[row][col] == "1"
        )


class SolutionBFS:
    """
    Notes
    -----
    - TC: O(mn)
    - SC: O(mn)
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid), len(grid[0])

        def bfs(start_row, start_col):
            queue = deque([(start_row, start_col)])
            grid[start_row][start_col] = "visited"

            while queue:
                current_row, current_col = queue.popleft()

                for dx, dy in directions:
                    new_row, new_col = current_row + dx, current_col + dy
                    if (
                        0 <= new_row < m
                        and 0 <= new_col < n
                        and grid[new_row][new_col] == "1"
                    ):
                        queue.append((new_row, new_col))
                        grid[new_row][new_col] = "visited"
            return 1

        return sum(
            bfs(row, col)
            for row in range(m)
            for col in range(n)
            if grid[row][col] == "1"
        )


if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    result_union_find = SolutionUnionFind().numIslands(grid)
    result_dfs = SolutionDFS().numIslands(copy.deepcopy(grid))
    result_bfs = SolutionDFS().numIslands(copy.deepcopy(grid))
    print(f"Union Find: {result_union_find}")
    print(f"DFS: {result_dfs}")
    print(f"BFS: {result_bfs}")
