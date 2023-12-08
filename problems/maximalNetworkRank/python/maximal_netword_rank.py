from collections import defaultdict
from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        """
        Complexity
        ----------
        TC: O(n^2)
        SC: O(n)
        """
        if len(roads) <= 1:
            return len(roads)

        graph = defaultdict(list)
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)

        max_roads = 1

        for node1 in range(n):
            for node2 in range(node1 + 1, n):
                num_roads1 = len(graph[node1])
                num_roads2 = len(graph[node2])

                if node1 in graph[node2]:
                    num_roads1 -= 1

                max_roads = max(max_roads, num_roads1 + num_roads2)

        return max_roads


if __name__ == "__main__":
    n = 4
    roads = [[0, 1], [0, 3], [1, 2], [1, 3]]
    print(f"Solution: {Solution().maximalNetworkRank(n, roads)}")
