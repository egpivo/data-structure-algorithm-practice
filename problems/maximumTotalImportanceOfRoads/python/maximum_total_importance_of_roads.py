from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n log n + m)
    - SC: O(n)
    """

    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1

        sorted_cities = sorted(range(n), key=lambda x: degree[x], reverse=True)

        values = [0] * n
        current = n
        for city in sorted_cities:
            values[city] = current
            current -= 1

        total_importance = 0
        for a, b in roads:
            total_importance += values[a] + values[b]

        return total_importance


if __name__ == "__main__":
    n = 5
    roads = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]
    print(f"The solution is {Solution().maximumImportance(n, roads)}")
