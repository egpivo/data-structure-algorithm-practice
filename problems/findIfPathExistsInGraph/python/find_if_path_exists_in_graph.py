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
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        """
        Time Complexity: O(V + E) ~ O(`n` + `n_edges`)
        Space Complexity: O(V + E) ~ O(`n` + `n_edges`)
        """
        collection = defaultdict(list)

        for x, y in edges:
            collection[x].append(y)
            collection[y].append(x)

        q = deque([start])
        marked = set([start])

        while q:
            node = q.popleft()
            if node == end:
                return True
            for child_node in collection[node]:
                if child_node not in marked:
                    marked.add(child_node)
                    q.append(child_node)
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
