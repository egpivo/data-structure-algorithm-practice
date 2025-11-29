import heapq
from typing import List


class Solution:
    """
    Complexity
    ----------
    - Time complexity: $O(k\log k)$
    - Space complexity: $O(k)$
    """

    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        result = []
        heap = []
        visited = set()

        increments = ((0, 1), (1, 0))
        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))
        visited.add((0, 0))

        while heap and len(result) < k:
            _, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])

            for dx, dy in increments:
                new_i, new_j = i + dx, j + dy
                if (
                    new_i < len(nums1)
                    and new_j < len(nums2)
                    and (new_i, new_j) not in visited
                ):
                    heapq.heappush(heap, (nums1[new_i] + nums2[new_j], new_i, new_j))
                    visited.add((new_i, new_j))

        return result


if __name__ == "__main__":
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 3
    print(f"Solution: {Solution().kSmallestPairs(nums1, nums2, k)}")
