from typing import Optional, List

# Definition
class UnionFind:
    def __init__(self, size: int):
        # used to check if the root is changed
        self.root = [-1] * size
        self.rank = [1] * size

    def find(self, x):
        if self.root[x] != -1:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[x] >= self.rank[y]:
                self.root[root_y] = root_x
                self.rank[x] += 1
            else:
                self.root[root_x] = root_y
                self.rank[y] += 1


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Time complexity: O(N^3)
        space complexity: O(N)
        """
        size = len(isConnected)
        uf = UnionFind(size)

        for i in range(size):
            for j in range(size):
                if i != j and isConnected[i][j] == 1:
                    uf.union(i, j)

        count = 0
        for i in range(size):
            if uf.root[i] == -1:
                count += 1
        return count

if __name__ == "__main__":
    isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    result = Solution().findCircleNum(isConnected)
    print(result)


