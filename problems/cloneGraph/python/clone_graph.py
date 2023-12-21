from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for src, dst in prerequisites:
            graph[src].append(dst)

        def dfs(src, visited, path, memo):
            if (src, path) in memo:
                return memo[(src, path)]

            if src in visited:
                return False
            if src not in graph:
                return True

            visited.add(src)
            result = True

            for neighbor in graph[src]:
                result &= dfs(neighbor, visited, path + 1, memo)

            visited.remove(src)
            memo[(src, path)] = result
            return result

        for key in range(numCourses):
            is_valid = dfs(key, set(), 0, {})
            if not is_valid:
                return False
        return True
