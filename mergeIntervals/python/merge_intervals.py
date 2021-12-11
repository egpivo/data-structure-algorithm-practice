from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        new_intervals = []

        for interval in intervals:
            if new_intervals and new_intervals[-1][1] >= interval[0]:
                new_intervals[-1][1] = max(new_intervals[-1][1], interval[1])
            else:
                new_intervals.append(interval)
        return new_intervals


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(f"Solution is {Solution().merge(intervals)}")
