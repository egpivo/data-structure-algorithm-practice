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
        
        
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        
        for i in range(n):
            for j in range(i, n):
                if i != j and isConnected[i][j] == 1:
                    uf.union(i, j)
        return len(set(uf.root))


if __name__ == "__main__":
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    result = Solution().findCircleNum(isConnected)
    print(result)


