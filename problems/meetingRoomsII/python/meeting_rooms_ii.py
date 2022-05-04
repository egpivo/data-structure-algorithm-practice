import heapq
from typing import List


class Solution:
    """

    Complexity
    ----------
    - TC: O(n*long(n))
    - SC: O(n)
    """

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        used_rooms = [intervals[0][1]]
        heapq.heapify(used_rooms)

        for interval in intervals[1:]:
            if used_rooms[0] <= interval[0]:
                heapq.heappop(used_rooms)

            heapq.heappush(used_rooms, interval[1])

        return len(used_rooms)


if __name__ == "__main__":
    intervals = [[0, 30], [5, 10], [15, 20]]
    print(f"Solution is {Solution().minMeetingRooms(intervals)}")
