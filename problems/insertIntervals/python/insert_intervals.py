from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n*long(n)) (sorting)
    - SC: O(n) (resultant output)
    """

    def insert(
        self, intervals: List[List[int]], new_interval: List[int]
    ) -> List[List[int]]:
        answer = []
        index = 0
        for interval in intervals:
            if new_interval[0] > interval[1]:
                answer.append(interval)
            else:
                break
            index += 1

        answer.append(new_interval)
        for interval in intervals[index:]:
            if interval[0] <= answer[-1][1]:
                answer[-1][0] = min(answer[-1][0], interval[0])
                answer[-1][1] = max(answer[-1][1], interval[1])
            else:
                answer.append(interval)
        return answer


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    new_interval = [4, 8]
    print(f"Solution is {Solution().insert(intervals, new_interval)}")
