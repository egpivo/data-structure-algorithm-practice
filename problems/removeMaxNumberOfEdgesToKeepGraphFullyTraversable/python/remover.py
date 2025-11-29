from typing import List


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False


class Solution:
    """
    Complexity
    ----------
    - TC: O(E \log V)
    - SC: O(V)
    """

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice_uf = UnionFind(n + 1)
        bob_uf = UnionFind(n + 1)

        edges_used = 0
        for edge_type, u, v in edges:
            if edge_type == 3:
                if alice_uf.union(u, v):
                    bob_uf.union(u, v)
                    edges_used += 1

        for edge_type, u, v in edges:
            if edge_type == 2:
                if alice_uf.union(u, v):
                    edges_used += 1

        for edge_type, u, v in edges:
            if edge_type == 2:
                if bob_uf.union(u, v):
                    edges_used += 1

        if (
            len(set(alice_uf.find(i) for i in range(1, n + 1))) != 1
            or len(set(bob_uf.find(i) for i in range(1, n + 1))) != 1
        ):
            return -1
        return len(edges) - edges_used


if __name__ == "__main__":
    n = 4
    edges = [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]
    print(f"The Solution is {Solution().maxNumEdgesToRemove(n, edges)}")
