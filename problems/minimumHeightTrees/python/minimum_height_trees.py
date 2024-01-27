from collections import defaultdict
from typing import List


class Solution:
    """
    Complexity
    ----------
    - SC: O(V+E)
    - TC: O(V+E)
    """

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Function to perform DFS and find the node with maximum distance
        def dfs(node, parents):
            max_distance_pair = (-1, node)
            for neighbor in graph[node]:
                if neighbor != parents[node]:
                    parents[neighbor] = node
                    max_distance_pair = max(max_distance_pair, dfs(neighbor, parents))
            return max_distance_pair[0] + 1, max_distance_pair[1]

        # Find the vertex on the boundary given a random node with maximum distance
        parents = [-1] * n
        _, vertex1 = dfs(0, parents)  # Using 0 as the random starting node

        # Find the other vertex on the boundary given the vertex on the boundary with maximum distance
        parents = [-1] * n
        diameter, vertex2 = dfs(vertex1, parents)

        # Find the center(s)
        for _ in range(diameter // 2):
            vertex2 = parents[vertex2]

        # If the diameter is even, return a list with one vertex, else return a list with two vertices
        return [vertex2] if diameter % 2 == 0 else [vertex2, parents[vertex2]]
