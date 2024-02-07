from typing import List


class Solution:
    """
    The dp[i][0] represents the minimum swaps needed at position i when no swap is performed,
    and dp[i][1] represents the minimum swaps needed when a swap is performed.
    """

    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[float("inf"), float("inf")] for i in range(len(nums1))]

        dp[0][0] = 0
        dp[0][1] = 1

        for i in range(1, len(dp)):
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                dp[i][0] = min(dp[i][0], dp[i - 1][0])
                dp[i][1] = min(dp[i][1], dp[i - 1][1] + 1)
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                dp[i][0] = min(dp[i][0], dp[i - 1][1])
                dp[i][1] = min(dp[i][1], dp[i - 1][0] + 1)
        return min(dp[-1])


if __name__ == "__main__":
    nums1 = [0, 7, 8, 10, 10, 11, 12, 13, 19, 18]
    nums2 = [4, 4, 5, 7, 11, 14, 15, 16, 17, 20]
    print(f"Solution: {Solution().minSwap(nums1, nums2)}")
