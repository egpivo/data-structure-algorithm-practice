from typing import List
import random


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Complexity
        ---------
        - TC: O(NlogN) (due to the sort with the worst case)
        - SC: O(1)
        """
        return [point for point in sorted(points, key=lambda x: x[0] * x[0] + x[1] * x[1])][:k]


class SolutionQuickSort:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Complexity
        ---------
        - TC: O(NlogN) (due to the sort with the worst case)
        - SC: O(1)
        """

        def partition(points, left, right, pivot):
            pivot_sum = points[pivot][0] ** 2 + points[pivot][1] ** 2
            points[pivot], points[right] = points[right], points[pivot]

            s = left
            for index in range(left, right):
                index_sum = points[index][0] ** 2 + points[index][1] ** 2
                if index_sum < pivot_sum:
                    points[index], points[s] = points[s], points[index]
                    s += 1
            points[s], points[right] = points[right], points[s]
            return s

        def quickSelect(points, left, right):
            pivot = random.randint(left, right)
            mid = partition(points, left, right, pivot)

            if mid == k - 1:
                return points[:(mid + 1)]
            elif mid > k - 1:
                quickSelect(points, left, mid + 1)
            else:
                quickSelect(points, mid + 1, right)

        return quickSelect(points, 0, len(points) - 1)


if __name__ == "__main__":
    array = [[1, 3], [-2, 2]]
    k = 1
    print(f"The answer is {Solution().kClosest(array, k)}")
    print(f"The answer is {SolutionQuickSort().kClosest(array, k)}")
