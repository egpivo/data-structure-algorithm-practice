from collections import defaultdict
from typing import List


class Solution:
    """
    Complexity
    ----------
    - Time complexity: $O(n^2)$
    - Space complexity:: $O(n\cdot m)$
    """

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        total_count = 0
        dp = [defaultdict(int) for _ in range(n)]

        for i in range(1, n):
            for j in range(i):
                difference = nums[i] - nums[j]
                step_count = dp[j][difference]
                dp[i][difference] = dp[i][difference] + step_count + 1
                total_count += step_count

        return total_count


if __name__ == "__main__":
    nums = [2, 4, 6, 8, 10]
    print(f"Solution: {Solution().numberOfArithmeticSlices(nums)}")
