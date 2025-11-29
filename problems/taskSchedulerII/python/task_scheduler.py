from typing import List


class Solution:
    """
    Complexity
    ----------
    - O(N)
        - N is the number of tasks
    - O(N)
    """

    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        last_occurrence = {}
        cumulative_days = 0

        for task in tasks:
            cumulative_days = (
                max(cumulative_days + 1, last_occurrence[task] + space + 1)
                if task in last_occurrence
                else cumulative_days + 1
            )
            last_occurrence[task] = cumulative_days

        return cumulative_days


if __name__ == "__main__":
    tasks = [1, 2, 1, 2, 3, 1]
    space = 2
    print(Solution().taskSchedulerII(tasks, space))
