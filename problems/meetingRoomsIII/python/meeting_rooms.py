import heapq
from collections import defaultdict
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n\log(n))
    - SC: O(n)
    """

    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        booked, free = [], list(range(n))
        freq = defaultdict(int)

        for start, end in meetings:
            while booked and booked[0][0] <= start:
                _, room = heapq.heappop(booked)
                heapq.heappush(free, room)

            if free:
                room = heapq.heappop(free)
                heapq.heappush(booked, (end, room))
            else:
                release, room = heapq.heappop(booked)
                heapq.heappush(booked, (release + end - start, room))

            freq[room] += 1

        return max(freq, key=freq.get)


if __name__ == "__main__":
    n = 3
    meetings = [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]
    print(Solution().mostBooked(n, meetings))
