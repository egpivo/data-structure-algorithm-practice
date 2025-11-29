from typing import List


class Solution:
    """
    - TC: O(n)
    - SC: O(1)
    """

    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)

        count = 0
        left = 0
        for right in range(n):
            if right > 0 and prices[right] - prices[right - 1] != -1:
                left = right
            count += right - left + 1

        return count


if __name__ == "__main__":
    prices = [3, 2, 1, 4]
    instance = Solution()

    print(f"Test answer: {instance.getDescentPeriods(prices)}")
