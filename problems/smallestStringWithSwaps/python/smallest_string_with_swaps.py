from collections import defaultdict
from typing import List

class UnionFind:
    def __init__(self, size):
        self.root = list(range(size))
        
    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        self.root[self.find(y)] = self.find(x)


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n)
        
        for x, y in pairs:
            uf.union(x, y)
            
        temp_dict = defaultdict(list)
        
        for i in range(n):
            temp_dict[uf.find(i)].append(s[i])
        
        for key in temp_dict:
            temp_dict[key].sort()
        
        res = []
        for i in range(n):
            res.append(temp_dict[uf.find(i)].pop(0))
        return ''.join(res)
        
        
        
if __name__ == "__main__":
    s = "dcab"
    pairs = [[0,3],[1,2],[0,2]]
    print(Solution().smallestStringWithSwaps(s, pairs))