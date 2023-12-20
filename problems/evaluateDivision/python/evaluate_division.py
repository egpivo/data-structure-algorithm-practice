from typing import List, Tuple


class UnionFind:
    def __init__(self) -> None:
        self.root = {}

    def find(self, x) -> Tuple[str, float]:
        if x not in self.root:
            self.root[x] = (x, 1)
        group_id, weight = self.root[x]
        if group_id != x:
            new_group_id, group_weight = self.find(group_id)
            self.root[x] = (new_group_id, group_weight * weight)
        return self.root[x]

    def union(self, x, y, weight) -> None:
        root_x, weight_x = self.find(x)
        root_y, weight_y = self.find(y)

        if root_x != root_y:
            self.root[root_x] = (root_y, weight_y * weight / weight_x)


class Solution:
    """
    - Time Complexity:
       - The time complexity is determined by the operations on the Union-Find data structure.
       - The find and union operations have an amortized time complexity of approximately O(1), making the overall time complexity linear in the number of equations and queries.
    - Space Complexity:
       - The space complexity is determined by the Union-Find data structure, which uses extra space proportional to the number of variables (equations).
       - The overall space complexity is linear in the number of equations.
    """

    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        uf = UnionFind()
        for (x, y), weight in zip(equations, values):
            uf.union(x, y, weight)

        results = []
        for x, y in queries:
            if x not in uf.root or y not in uf.root:
                results.append(-1.0)
            else:
                root_x, weight_x = uf.find(x)
                root_y, weight_y = uf.find(y)
                if root_x != root_y:
                    results.append(-1)
                else:
                    results.append(weight_x / weight_y)
        return results
