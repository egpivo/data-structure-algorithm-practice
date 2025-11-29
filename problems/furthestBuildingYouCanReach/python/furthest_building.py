import heapq
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n\log(ladders))
    - SC: O(ladders)
    """

    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        min_heap = []

        for i in range(n - 1):
            diff = heights[i + 1] - heights[i]

            if diff > 0:
                heapq.heappush(min_heap, diff)

                if len(min_heap) > ladders:
                    bricks -= heapq.heappop(min_heap)

                if bricks < 0:
                    return i

        return n - 1


if __name__ == "__main__":
    heights = [4, 2, 7, 6, 9, 14, 12]
    bricks = 5
    ladders = 1
    print(f"The solution is {Solution().furthestBuilding(heights, bricks, ladders)}")
