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


class Solution2:
    """
    Complexity
    ----------
    - TC: O(n*long(n)) (sorting)
    - SC: O(1)
    """

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # Sort the points based on their end positions
        points.sort(key=lambda x: x[1])

        arrows = 1  # Initialize the number of arrows
        prev_end = points[0][1]  # Initialize the end position of the first point

        # Iterate through the points
        for start, end in points[1:]:
            # If the current start position is greater than the previous end position,
            # increment the arrow count and update the previous end position
            if start > prev_end:
                arrows += 1
                prev_end = end

        return arrows


if __name__ == "__main__":
    intervals = [[10, 16], [2, 8], [1, 6], [7, 12]]
    print(f"Solution is {Solution().findMinArrowShots(intervals)}")
    print(f"Solution2 is {Solution().findMinArrowShots(intervals)}")
