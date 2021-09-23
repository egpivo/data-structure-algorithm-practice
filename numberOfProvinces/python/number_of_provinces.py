from collections import deque
from typing import Optional, List


class UnionFind:
    """
    Note
    ----
    - We can only use quick find instead of quick union
    """

    def __init__(self, size):
        self.size = size
        self.root = [i for i in range(size)]

    def find(self, x):
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            for i in range(self.size):
                if self.root[i] == root_y:
                    self.root[i] = root_x


class SolutionUnionFind:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i, n):
                if i != j and isConnected[i][j] == 1:
                    uf.union(i, j)
        return len(set(uf.root))


class SolutionDFS:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        marked = set()

        def dfs(start):
            for i in range(n):
                if isConnected[start][i] == 1 and i not in marked:
                    marked.add(i)
                    dfs(i)

        count = 0
        for i in range(n):
            if i not in marked:
                dfs(i)
                count += 1

        return count

class SolutionBFS:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        marked = set()
        def bfs(start):
            q = deque([start])
            while q:
                node = q.popleft()
                for i in range(n):
                    if isConnected[node][i] == 1 and i not in marked:
                        marked.add(i)
                        q.append(i)
                    
        count = 0
        for i in range(n):
            if i not in marked:
                bfs(i)
                count += 1
        
        return count



if __name__ == "__main__":
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    result_union_find = SolutionUnionFind().findCircleNum(isConnected)
    result_dfs = SolutionDFS().findCircleNum(isConnected)
    result_bfs = SolutionBFS().findCircleNum(isConnected)    
    print(f"Union Find: {result_union_find}")
    print(f"DFS: {result_dfs}")
    print(f"BFS: {result_bfs}")    

