import heapq
from typing import List


class Solution:
    """
    @param arr: an array of integers
    @param k: an integer
    @return: the Kth smallest element in a specific array
    """

    def kth_smallest(self, arr: List[List[int]], k: int) -> int:
        # write your code here
        output = []

        for nums in arr:
            for num in nums:
                heapq.heappush(output, -num)
                if len(output) > k:
                    heapq.heappop(output)
        return -output[0]


if __name__ == "__main__":
    matrix = [[1, 5, 7, 9], [3, 4], [2, 7, 8]]
    k = 5
    print(f"Solution: {Solution().kth_smallest(matrix, k)}")
