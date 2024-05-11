import heapq
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n\log n)
    - SC: O(k)
    """

    def mincostToHireWorkers(
        self, qualities: List[int], wages: List[int], k: int
    ) -> float:
        # Sort workers by wage-to-quality ratio
        workers = sorted(
            [(wage / quality, quality) for wage, quality in zip(wages, qualities)],
            key=lambda x: x[0],
        )
        quality_heap = []  # Min-heap to track k workers with lowest quality
        total_quality = 0  # Total quality of workers in heap

        # Initialize heap with the first k workers and calculate initial total quality
        for ratio, quality in workers[:k]:
            heapq.heappush(
                quality_heap, -quality
            )  # Use negative quality to maintain min-heap property
            total_quality += quality

        # Calculate initial minimum cost
        min_cost = total_quality * workers[k - 1][0]

        # Iterate over remaining workers
        for ratio, quality in workers[k:]:
            # Update total quality by adding current worker and removing lowest quality worker from heap
            total_quality += quality + heapq.heappop(quality_heap)
            heapq.heappush(
                quality_heap, -quality
            )  # Push current worker's quality onto heap
            # Update minimum cost if necessary
            min_cost = min(min_cost, total_quality * ratio)

        return min_cost


if __name__ == "__main__":
    quality = [10, 20, 5]
    wage = [70, 50, 30]
    k = 2
    print(f"The solution is {Solution().mincostToHireWorkers(quality, wage, k)}")
