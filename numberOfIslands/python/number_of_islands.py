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
    def numIslands(self, grid: List[List[str]]) -> int:
        nrow = len(grid)
        ncol = len(grid[0])

        def dfs(i, j):
            if not (0 <= i < nrow) or not (0 <= j < ncol) or grid[i][j] != "1":
                return
            grid[i][j] = "#"
            dfs(i, j + 1)
            dfs(i, j - 1)
            dfs(i - 1, j)
            dfs(i + 1, j)

        count = 0
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count


class SolutionBFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        nrow = len(grid)
        ncol = len(grid[0])

        def bfs(i, j):
            queue = deque([(i, j)])
            while queue:
                i, j = queue.popleft()
                for k, m in [i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]:
                    if (0 <= k < nrow) and (0 <= m < ncol) and (grid[k][m] == "1"):
                        grid[k][m] = "#"
                        queue.append((k, m))

        count = 0
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == "1":
                    grid[i][j] = "#"
                    bfs(i, j)
                    count += 1
        return count


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

