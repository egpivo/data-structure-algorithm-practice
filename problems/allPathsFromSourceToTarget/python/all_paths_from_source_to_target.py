from collections import deque


class DFS:
    def allPathsSourceTarget(self, graph):
        n = len(graph)
        ans = []

        def dfs(start, path):
            if start == n - 1:
                ans.append(path + [start])
                return
            for child in graph[start]:
                dfs(child, path + [start])

        dfs(0, [])
        return ans


class BFS:
    def allPathsSourceTarget(self, graph):
        """
        Time Complexity: O(V + E) ~ O(`n` + `n_edges`)
        Space Complexity: O(V + E) ~ O(`n` + `n_edges`)
        """
        n = len(graph)
        q = deque()
        q.append([0])
        ans = []

        while q:
            node = q.popleft()
            if node[-1] == n - 1:
                ans.append(node)

            for child_node in graph[node[-1]]:
                q.append(node + [child_node])

        return ans


if __name__ == "__main__":
    graph = [[1, 2], [3], [3], []]
    result_dfs = DFS().allPathsSourceTarget(graph)
    result_bfs = BFS().allPathsSourceTarget(graph)
    print(f"DFS: {result_dfs}")
    print(f"BFS: {result_bfs}")
    assert result_dfs == result_bfs, "Wrong results"
