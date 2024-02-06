from collections import deque
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0] * n

        for node in range(n):
            if colors[node] != 0:
                continue

            queue = deque([node])
            colors[node] = 1

            while queue:
                node = queue.popleft()

                for neighbor in graph[node]:
                    if colors[neighbor] == 0:
                        colors[neighbor] = -colors[node]
                        queue.append(neighbor)
                    elif colors[neighbor] == colors[node]:
                        return False
        return True


if __name__ == "__main__":
    graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
    print(Solution().isBipartite(graph))
