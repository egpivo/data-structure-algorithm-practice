from collections import defaultdict, deque
from typing import List


class Solution:
    """
    Notes
    -----
    - TC: O(V + E)
    - SC: O(V + E)
    """

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses <= 1:
            return [0]
        if not prerequisites:
            return list(range(numCourses))

        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for target, source in prerequisites:
            graph[source].append(target)
            in_degree[target] += 1

        queue = deque(
            [course for course in range(numCourses) if in_degree[course] == 0]
        )
        result = []

        while queue:
            course = queue.popleft()
            result.append(course)

            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return result if len(result) == numCourses else []
