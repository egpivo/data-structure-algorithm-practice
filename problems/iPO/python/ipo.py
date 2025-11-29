import heapq
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n\log n + k \log n)
    - SC: O(n)
    """

    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        projects = list(zip(capital, profits))
        projects.sort()

        max_heap = []
        index = 0
        n = len(projects)

        for _ in range(k):
            # Push all projects we can afford into the max-heap
            while index < n and projects[index][0] <= w:
                # Use negative profit for max-heap
                heapq.heappush(max_heap, -projects[index][1])
                index += 1

            if not max_heap:
                break

            w -= heapq.heappop(max_heap)

        return w


if __name__ == "__main__":
    k = 2
    w = 0
    profits = [1, 2, 3]
    capital = [0, 1, 1]
    print(f"The solution is {Solution().findMaximizedCapital(k, w, profits, capital)}")
