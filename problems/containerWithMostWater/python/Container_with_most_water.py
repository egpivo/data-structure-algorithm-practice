class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left, right, area = 0, len(height) - 1, 0

        while left < right:

            minHeight = min(height[left], height[right])
            area = max(area, minHeight * (right - left))

            while left < right and minHeight == height[left]:
                left += 1
            while left < right and minHeight == height[right]:
                right -= 1

        return area


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(Solution().maxArea(height))
