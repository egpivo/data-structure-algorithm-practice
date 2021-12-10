import heapq
from typing import List


class Solution:
    """

    Complexity
    ----------
    - TC: O(min(k, nrows) + k log(min(k, nrow)))
    - SC: O(min(k, nrows)
    """

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nrows = len(matrix)

        min_heap = []
        for row in range(min(k, nrows)):
            min_heap.append((matrix[row][0], row, 0))

        heapq.heapify(min_heap)

        while k:
            element, row, col = heapq.heappop(min_heap)
            if col < len(matrix[row]) - 1:
                heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))

            k -= 1

        return element


if __name__ == "__main__":
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    print(f"Solution: {Solution().kthSmallest(matrix, k)}")
