import bisect
from typing import List


class Solution:
    """
    Complexity
    ----------
    - Time complexity: $O(n\log n)$
    - Space complexity: $O(n)$
    """

    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        sorted_end_times = [x[1] for x in jobs]
        n = len(jobs)

        dp = [0] * n
        dp[0] = jobs[0][2]

        for i in range(1, n):
            current_start, current_profit = jobs[i][0], jobs[i][2]
            # Find the latest job that finishes before the current job starts
            j = bisect.bisect_right(sorted_end_times, current_start) - 1
            if j >= 0:
                current_profit += dp[j]

            dp[i] = max(current_profit, dp[i - 1])

        return dp[-1]


if __name__ == "__main__":
    startTime = [1, 2, 3, 3]
    endTime = [3, 4, 5, 6]
    profit = [50, 10, 40, 70]
    print(f"Solution: {Solution().jobScheduling(startTime, endTime, profit)}")
