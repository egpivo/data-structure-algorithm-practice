from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n*long(n)) (sorting)
    - SC: O(1)
    """
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return len(points)

        points.sort(key=lambda x: x[0])
        count = 1
        min_right = points[0][1]

        for point in points[1:]:
            if min_right >= point[0]:
                min_right = min(min_right, point[1])
            else:
                min_right = point[1]
                count += 1
        return count


if __name__ == "__main__":
    intervals = [[10,16],[2,8],[1,6],[7,12]]
    print(f"Solution is {Solution().findMinArrowShots(intervals)}")

