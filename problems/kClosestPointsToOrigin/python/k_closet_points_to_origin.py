import heapq
import random
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Complexity
        ---------
        - TC: O(NlogN) (due to the sort with the worst case)
        - SC: O(1)
        """
        return [point for point in sorted(points, key=lambda x: x[0] * x[0] + x[1] * x[1])][:k]


class SolutionPriorityQueue:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Complexity
        ---------
        - TC: O(Nlogk)
        - SC: O(k)
        """
        distance_heap = [(self.negative_squared_distance(points[i]), i) for i in range(k)]
        heapq.heapify(distance_heap)

        for i in range(k, len(points)):
            distance = self.negative_squared_distance(points[i])
            if distance > distance_heap[0][0]:
                heapq.heappushpop(distance_heap, (distance, i))

        return [points[i] for _, i in distance_heap]

    def negative_squared_distance(self, point: List[int]) -> int:
        return - sum(x ** 2 for x in point)


class SolutionQuickSort:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Complexity
        ---------
        - TC: O(N) (avg; a worst-case time complexity of O(N^2))
        - SC: O(1)
        """

        def partition(points, left, right, pivot):
            pivot_sum = self.squared_distance(points[pivot])
            points[pivot], points[right] = points[right], points[pivot]

            s = left
            for index in range(left, right):
                index_sum = self.squared_distance(points[index])
                if index_sum < pivot_sum:
                    points[index], points[s] = points[s], points[index]
                    s += 1
            points[s], points[right] = points[right], points[s]

            return s

        def quick_select(points, left, right):
            pivot = random.randint(left, right)
            mid = partition(points, left, right, pivot)

            if mid == k - 1:
                return points[:k]
            elif mid > k - 1:
                return quick_select(points, left, mid - 1)
            else:
                return quick_select(points, mid + 1, right)

        return quick_select(points, 0, len(points) - 1)

    def squared_distance(self, point: List[int]) -> int:
        return sum(x ** 2 for x in point)


if __name__ == "__main__":
    array = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    print(f"The answer is {Solution().kClosest(array, k)}")
    print(f"The answer is {SolutionPriorityQueue().kClosest(array, k)}")
    print(f"The answer is {SolutionQuickSort().kClosest(array, k)}")
