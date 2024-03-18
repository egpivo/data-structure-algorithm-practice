from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n*long(n)) (sorting)
    - SC: O(1)
    """

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        overlaps = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prev_end:  # Check for overlapping intervals
                overlaps += 1
                prev_end = min(
                    prev_end, end
                )  # Update the end to the minimum of current end and previous end
            else:
                prev_end = end  # Update the end to the current end

        return overlaps


class Solution2:
    """
    Complexity
    ----------
    - TC: O(n*long(n)) (sorting)
    - SC: O(1)
    """

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])  # Sort intervals by end points

        overlaps = 0
        prev_end = intervals[0][1]  # Initialize previous end point

        for start, end in intervals[1:]:
            if start < prev_end:  # Check for overlapping intervals
                overlaps += 1
            else:
                prev_end = end  # Update previous end point if no overlap

        return overlaps


if __name__ == "__main__":
    intervals = [[10, 16], [2, 8], [1, 6], [7, 12]]
    print(f"Solution is {Solution().eraseOverlapIntervals(intervals)}")
    print(f"Solution2 is {Solution().eraseOverlapIntervals(intervals)}")
