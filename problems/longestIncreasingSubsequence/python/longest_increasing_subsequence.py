from bisect import bisect_left
from typing import List


class Solution:
    """
    Complexity
    ----------
    - Time complexity: $O(n^2)$
    - Space complexity: $O(n)$
    """

    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


class Solution2:
    """
    Complexity
    ----------
    - Time complexity: $O(n\log(n))$
    - Space complexity: $O(n)$
    """

    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        result = []

        for num in nums:
            position = bisect_left(result, num)

            if position == len(result):
                result.append(num)
            else:
                result[position] = num

        return len(result)


if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(f"Solution: {Solution().lengthOfLIS(nums)}")
    print(f"Solution: {Solution2().lengthOfLIS(nums)}")
