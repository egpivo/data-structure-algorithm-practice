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

        max_count = sum(grid[i][j] == '1' for i in range(nrow) for j in range(ncol))
        uf = UnionFind(nrow * ncol, max_count)

        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == '0':
                    continue
                index = i * ncol + j
                if j < ncol -1 and grid[i][j + 1] == '1':
                    uf.union(index, index + 1)
                if i < nrow - 1 and grid[i + 1][j] == '1':
                    uf.union(index, index + ncol)

        return uf.max_count

if __name__ == "__main__":
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    result = SolutionUnionFind().numIslands(grid)
    print(result)


