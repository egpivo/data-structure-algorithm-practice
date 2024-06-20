from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n\log(n) + nlog(position[−1]−position[0]))
    - SC: O(1)
    """

    def maxDistance(self, position: List[int], m: int) -> int:
        # Sort positions to apply binary search
        position.sort()

        # Binary search on the answer
        left, right = 1, position[-1] - position[0]
        best = 0

        while left <= right:
            mid = (left + right) // 2
            if self.canPlaceBalls(mid, position, m):
                best = mid
                left = mid + 1
            else:
                right = mid - 1

        return best

    def canPlaceBalls(self, min_dist, position, m):
        # Place the first ball in the first basket
        count = 1
        last_pos = position[0]

        for i in range(1, len(position)):
            if position[i] - last_pos >= min_dist:
                count += 1
                last_pos = position[i]
                if count == m:
                    return True
        return False


if __name__ == "__main__":
    matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
    print(f"{Solution().minFallingPathSum(matrix)}")
