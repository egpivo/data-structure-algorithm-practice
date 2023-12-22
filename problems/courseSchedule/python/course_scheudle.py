from collections import defaultdict, deque
from typing import List


class SolutionDFS:
    """
    Notes
    -----
    - TC: O(V + E)
    - SC: O(V + E)
    """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0:
            return True

        graph = defaultdict(list)

        for course, precourse in prerequisites:
            graph[precourse].append(course)

        def is_valid(course, visited, path, memory):
            if (course, path) in memory:
                return memory[(course, path)]
            if not course in graph:
                return True

            visited.add(course)
            result = True
            for neighbor in graph[course]:
                if neighbor in visited or not is_valid(
                    neighbor, visited, path + 1, memory
                ):
                    result = False
                    break
            visited.remove(course)
            memory[(course, path)] = result
            return memory[(course, path)]

        for course in graph:
            if not is_valid(course, set(), 0, dict()):
                return False
        return True


class SolutionBFS:
    """
    Notes
    -----
    - TC: O(V + E)
    - SC: O(V + E)
    """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0:
            return True
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        queue = deque(course for course in range(numCourses) if in_degree[course] == 0)
        visited = set()

        while queue:
            current_course = queue.popleft()
            visited.add(current_course)

            for neighbor in graph[current_course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return len(visited) == numCourses
