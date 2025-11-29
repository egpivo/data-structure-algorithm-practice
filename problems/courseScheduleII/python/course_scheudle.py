from collections import defaultdict, deque
from typing import List


class SolutionDFS:
    """
    Notes
    -----
    - TC: O(V + E)
    - SC: O(V + E)
    """

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0:
            return [0]

        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visiting = set()
        visited = set()
        result = []

        def is_valid(course):
            nonlocal result, visiting, visited

            if course in visiting:
                return False
            if course in visited:
                return True

            visiting.add(course)

            for neighbor in graph[course]:
                if not is_valid(neighbor):
                    return False

            visiting.remove(course)
            visited.add(course)
            result.append(course)
            return True

        for course in range(numCourses):
            if course not in visited and not is_valid(course):
                return []

        return result[::-1]


class SolutionBFS:
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
        in_degrees = [0] * numCourses

        for target, source in prerequisites:
            graph[source].append(target)
            in_degrees[target] += 1

        queue = deque(
            [course for course in range(numCourses) if in_degrees[course] == 0]
        )
        result = []

        while queue:
            course = queue.popleft()
            result.append(course)

            for neighbor in graph[course]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)

        return result if len(result) == numCourses else []


if __name__ == "__main__":
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(f"DFS Solution: {SolutionDFS().findOrder(numCourses, prerequisites)}")
    print(f"BFS Solution: {SolutionBFS().findOrder(numCourses, prerequisites)}")
