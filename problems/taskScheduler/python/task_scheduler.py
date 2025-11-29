from collections import Counter
from typing import List


class Solution:
    """
    Complexity
    ----------
    - O(N+M)
        - N is the number of tasks
        - M is the number of unique tasks.
    - O(N)
    """

    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        frequencies = list(Counter(tasks).values())
        most_frequent = max(frequencies)
        most_frequent_tasks = frequencies.count(most_frequent)

        intervals = (most_frequent - 1) * (n + 1) + most_frequent_tasks
        return max(intervals, len(tasks))


if __name__ == "__main__":
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    print(Solution().leastInterval(tasks, n))
