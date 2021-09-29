from typing import List

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        
    def find(self, x):
        return self.root[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            for index, node in enumerate(self.root):
                if node == root_y:
                    self.root[index] = root_x


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        uf = UnionFind(n)
        for timestamp, x, y in sorted(logs):
            uf.union(x, y)
            if len(set(uf.root)) == 1:
                return timestamp
        return -1
        
if __name__ == "__main__":
    logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]]
    n = 4

    print(Solution().earliestAcq(logs, n))