from collections import defaultdict, deque
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


class Solution2:
    """
    Complexity
    ----------
    - SC: O(V)
    - TC: O(V+E)
    """

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        # Initialize the graph
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        # Perform BFS starting from leaves until only root(s) remain
        leaves = deque(node for node in graph if len(graph[node]) == 1)
        while n > 2:
            # Trim leaves level by level until only root(s) remain
            size = len(leaves)
            n -= size
            for _ in range(size):
                leaf = leaves.popleft()
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    leaves.append(neighbor)

        return list(leaves)


if __name__ == "__main__":
    n = 4
    edges = [[1, 0], [1, 2], [1, 3]]
    print(f"DFS Solution: {Solution().findMinHeightTrees(n, edges)}")
    print(f"BFS Solution: {Solution2().findMinHeightTrees(n, edges)}")
