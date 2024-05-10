import heapq
from typing import List


class Solution:
    """
    - TC: O(n\log n)
    - SC: O(n)
    """

    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        heap = []

        # Initialize heap with the first element from each row
        for i in range(n - 1):
            heapq.heappush(heap, (arr[i] / arr[-1], i, n - 1))

        for _ in range(k - 1):
            a, i, j = heapq.heappop(heap)
            if j > i + 1:
                heapq.heappush(heap, (arr[i] / arr[j - 1], i, j - 1))

        _, i, j = heapq.heappop(heap)
        return [arr[i], arr[j]]


if __name__ == "__main__":
    arr = [1, 2, 3, 5]
    k = 3
    print(f"The solution is {Solution().kthSmallestPrimeFraction(arr, k)}")
