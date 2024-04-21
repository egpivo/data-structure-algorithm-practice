from collections import defaultdict, deque
from typing import List


class DFS:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        """
        Time Complexity: O(V + E) ~ O(`n` + `n_edges`)
        Space Complexity: O(V + E) ~ O(`n` + `n_edges`)
        """
        collection = defaultdict(list)

        for x, y in edges:
            collection[x].append(y)
            collection[y].append(x)

        marked = set()

        def dfs(start):
            if start == end:
                return True

            marked.add(start)

            for x in collection[start]:
                if x not in marked and dfs(x):
                    return True

            return False

        return dfs(start)


class BFS:
    """
    Time Complexity: O(V + E) ~ O(`n` + `n_edges`)
    Space Complexity: O(V + E) ~ O(`n` + `n_edges`)
    """

    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        if not edges:
            return source == destination

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        children = deque([source])
        visited = set()
        while children:
            node = children.popleft()
            if node == destination:
                return True
            if node not in visited:
                children.extend(graph[node])
                visited.add(node)
        return False


if __name__ == "__main__":
    n = 3
    edges = [[0, 1], [1, 2], [2, 0]]
    start = 0
    end = 2
    result_dfs = DFS().validPath(n, edges, start, end)
    result_bfs = BFS().validPath(n, edges, start, end)
    print(f"DFS: {result_dfs}")
    print(f"BFS: {result_bfs}")
    assert result_dfs == result_bfs, "Wrong results"
