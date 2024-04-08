from collections import deque
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_queue = deque(enumerate(students))
        sandwiches_queue = deque(sandwiches)
        visited = set()

        while sandwiches_queue:
            if sandwiches_queue[0] == students_queue[0][1]:
                sandwiches_queue.popleft()
                students_queue.popleft()
                visited.clear()
            else:
                idx, student = students_queue.popleft()
                if idx in visited:
                    return len(sandwiches_queue)
                visited.add(idx)
                students_queue.append((idx, student))
        return 0


if __name__ == "__main__":
    students = [1, 1, 1, 0, 0, 1]
    sandwiches = [1, 0, 0, 0, 1, 1]
    print(f"{Solution().countStudents(students, sandwiches)}")
