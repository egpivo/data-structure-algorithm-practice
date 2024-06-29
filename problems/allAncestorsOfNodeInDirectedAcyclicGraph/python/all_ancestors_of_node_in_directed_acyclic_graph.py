from collections import defaultdict
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC:
    - SC:
    """

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)

        ancestors = [set() for _ in range(n)]

        def dfs(node, start):
            for neighbor in graph[node]:
                if start not in ancestors[neighbor]:
                    ancestors[neighbor].add(start)
                    dfs(neighbor, start)

        for node in range(n):
            dfs(node, node)

        result = [sorted(list(ancestor_set)) for ancestor_set in ancestors]

        return result


if __name__ == "__main__":
    n = 8
    edges = [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]
    print(f"The solution is {Solution().getAncestors(n, edges)}")
