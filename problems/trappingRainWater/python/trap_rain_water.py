from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(1)
    """

    def trap(self, height: List[int]) -> int:
        # Not enough elements to trap water
        if not height or len(height) < 3:
            return 0

        n = len(height)
        left, right = 0, n - 1
        left_max, right_max = height[left], height[right]
        water_trapped = 0

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max < right_max:
                water_trapped += left_max - height[left]
                left += 1
            else:
                water_trapped += right_max - height[right]
                right -= 1

        return water_trapped


if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution().trap(height))
