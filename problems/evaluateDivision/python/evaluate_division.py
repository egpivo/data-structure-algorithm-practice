from typing import List, Tuple


class UnionFind:
    def __init__(self) -> None:
        self.root = {}

    def _update(self, node) -> Tuple[str, float]:
        root, node_weight = self.root[node]
        if root != node:
            new_root, new_weight = self.find(root)
            self.root[node] = (new_root, new_weight * node_weight)
        return self.root[node]

    def find(self, node) -> Tuple[str, float]:
        if node not in self.root:
            self.root[node] = (node, 1)
            return self.root[node]
        else:
            return self._update(node)

    def union(self, src, dst, weight) -> None:
        root_src, src_weight = self.find(src)
        root_dst, dst_weight = self.find(dst)

        if root_src != root_dst:
            self.root[root_src] = (root_dst, dst_weight * weight / src_weight)


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
        graph = UnionFind()
        for (dividend, divisor), quotient in zip(equations, values):
            graph.union(dividend, divisor, quotient)

        results = []
        for dividend, divisor in queries:
            if dividend not in graph.root or divisor not in graph.root:
                results.append(-1.0)
            else:
                root_dividend, dividend_weight = graph.find(dividend)
                root_divisor, divisor_weight = graph.find(divisor)
                if root_dividend != root_divisor:
                    results.append(-1.0)
                else:
                    results.append(dividend_weight / divisor_weight)
        return results


if __name__ == "__main__":
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(f"Answer is {Solution().calcEquation(equations, values, queries)}")
