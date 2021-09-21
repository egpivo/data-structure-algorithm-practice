from collections import defaultdict
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





if __name__ == "__main__":
    n = 3
    edges = [[0,1],[1,2],[2,0]]
    start = 0
    end = 2
    result = DFS().validPath(n, edges, start, end)
    print(result)


