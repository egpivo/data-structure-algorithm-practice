from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n \log n + m\log m)
    - SC: O(n)
    """

    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        jobs = sorted(zip(difficulty, profit), key=lambda x: x[0])
        worker.sort()

        total_profit = 0
        max_profit = 0
        job_index = 0

        for w in worker:
            while job_index < len(jobs) and w >= jobs[job_index][0]:
                max_profit = max(max_profit, jobs[job_index][1])
                job_index += 1
            total_profit += max_profit

        return total_profit


if __name__ == "__main__":
    difficulty = [2, 4, 6, 8, 10]
    profit = [10, 20, 30, 40, 50]
    worker = [4, 5, 6, 7]
    print(Solution().maxProfitAssignment(difficulty, profit, worker))
