from typing import List


class UnionFind:
    def __init__(self, size: int) -> None:
        self.root = [i for i in range(size)]

    def find(self, x) -> int:
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])

        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root[root_y] = root_x

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def minCostToSupplyWater(
        self, n: int, wells: List[int], pipes: List[List[int]]
    ) -> int:
        ordered_edges = []
        # add the virtual vertex (index with 0) along with the new edges.
        for index, weight in enumerate(wells):
            ordered_edges.append((weight, 0, index + 1))

        # add the existing edges
        for house_1, house_2, weight in pipes:
            ordered_edges.append((weight, house_1, house_2))

        # sort the entire edges by their weights
        ordered_edges.sort(key=lambda x: x[0])
        uf = UnionFind(n + 1)
        total_cost = 0
        for cost, house_1, house_2 in ordered_edges:
            # determine if we should add the new edge to the final MST
            if not uf.is_connected(house_1, house_2):
                uf.union(house_1, house_2)
                total_cost += cost

        return total_cost


if __name__ == "__main__":
    n = 3
    wells = [1, 2, 2]
    pipes = [[1, 2, 1], [2, 3, 1]]

    print(Solution().minCostToSupplyWater(n, wells, pipes))
