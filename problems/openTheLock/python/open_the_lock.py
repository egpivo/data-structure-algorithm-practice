from collections import deque
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(10^4)
    - SC: O(10^4)
    """

    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        if "0000" in visited:
            return -1

        queue = deque([("0000", 0)])

        while queue:
            current, count = queue.popleft()
            if current == target:
                return count

            for i in range(4):
                for increment in (1, -1):
                    new_digit = (int(current[i]) + increment) % 10
                    new_combination = current[:i] + str(new_digit) + current[i + 1 :]
                    if new_combination not in visited:
                        visited.add(new_combination)
                        queue.append((new_combination, count + 1))

        return -1


if __name__ == "__main__":
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"
    print(f"Solution: {Solution().openLock(deadends, target)}")
