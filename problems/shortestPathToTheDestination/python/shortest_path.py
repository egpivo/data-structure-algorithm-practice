from collections import defaultdict, deque
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(mn)
    - SC: O(mn)
    """

    def shortest_path(self, target_map: List[List[int]]) -> int:
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        m, n = len(target_map), len(target_map[0])

        queue = deque([(0, 0)])
        visited = defaultdict(int)

        while queue:
            row, col = queue.popleft()
            for dx, dy in directions:
                new_r, new_c = row + dx, col + dy
                if (
                    0 <= new_r < m
                    and 0 <= new_c < n
                    and (new_r, new_c) not in visited
                    and target_map[new_r][new_c] != 1
                ):
                    queue.append((new_r, new_c))
                    visited[(new_r, new_c)] = visited[(row, col)] + 1
                    if target_map[new_r][new_c] == 2:
                        return visited[(new_r, new_c)]
        return -1


if __name__ == "__main__":
    input = [[0, 0, 0], [0, 0, 1], [0, 0, 2]]
    print(Solution().shortest_path(input))
