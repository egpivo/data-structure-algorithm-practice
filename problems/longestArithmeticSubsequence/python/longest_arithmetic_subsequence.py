from collections import defaultdict
from typing import List

class Solution:
    """

    Note
    ----
    - This is a DP problem
        - Keep the previous arithmetic values and update them if a repeated value occurs
    """
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n

        dp = defaultdict(dict)
        longest = 1

        for i in range(1, n):
            for j in range(i):
                difference = nums[i] - nums[j]
                if difference not in dp[j]:
                    dp[i][difference] = 2
                else:
                    dp[i][difference] = dp[j][difference] + 1
                longest = max(longest, dp[i][difference])
        return longest


if __name__ == "__main__":
    nums = [20, 1, 15, 3, 10, 5, 8]
    print(f"{Solution().longestArithSeqLength(nums)}")
