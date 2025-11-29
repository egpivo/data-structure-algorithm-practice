from collections import defaultdict, deque
class BfsSolution:
    """
    Time Complexity: O(V + E)
    Space Complexity: O(V + E)
    """
    def countComponents(self, n, edges):
        graph = defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        seen = set()
        connected = 0
        for node in range(n):
            if node in seen:
                continue
            connected += 1
            q = deque([node])
            seen.add(node)
            while q:
                current = q.popleft()          
                for child in graph[current]:
                    if child not in seen:
                        seen.add(child)
                        q.append(child)              
        return connected

class DfsSolution:
    """
    Time Complexity: O(V + E)
    Space Complexity: O(V + E)
    """
    def countComponents(self, n, edges):
        graph = defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        
        seen = set()
        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            for child in graph[node]:
                dfs(child)
        
        connected = 0
        for node in range(n):
            if node in seen:
                continue
            connected += 1
            dfs(node)
        return connected


if __name__ == "__main__":
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    solution = BfsSolution()
    print(solution.countComponents(n, edges))
        
    solution = DfsSolution()
    print(solution.countComponents(n, edges))