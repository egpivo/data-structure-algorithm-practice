from collections import defaultdict
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # Construct the graph from the edges
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Initialize lists to store subtree count and total distance sum
        subtree_count = [1] * n  # Count of nodes in the subtree rooted at each node
        total_distance = [0] * n  # Total distance sum rooted at each node

        # First DFS to calculate subtree_count and total_distance
        def dfs(node, parent):
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs(neighbor, node)
                    subtree_count[node] += subtree_count[neighbor]
                    total_distance[node] += (
                        total_distance[neighbor] + subtree_count[neighbor]
                    )

        # Second DFS to update total_distance for all nodes
        def dfs2(node, parent):
            for neighbor in graph[node]:
                if neighbor != parent:
                    total_distance[neighbor] = (
                        total_distance[node]
                        - subtree_count[neighbor]
                        + (n - subtree_count[neighbor])
                    )
                    dfs2(neighbor, node)

        dfs(0, -1)
        dfs2(0, -1)

        return total_distance


if __name__ == "__main__":
    n = 6
    edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
    print(f"The solution is {Solution().sumOfDistancesInTree(n, edges)}")
