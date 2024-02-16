from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        # dp[i][0]: Minimum swaps to make nums1[0:i+1] and nums2[0:i+1] increasing without swapping the i-th element.
        # dp[i][1]: Minimum swaps to make nums1[0:i+1] and nums2[0:i+1] increasing by swapping the i-th element.
        dp = [[float("inf"), float("inf")] for _ in range(n)]

        # Base cases
        dp[0][0] = 0
        dp[0][1] = 1

        for i in range(1, n):
            # If we don't swap i-th element, both arrays should be in increasing order.
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                dp[i][0] = min(dp[i][0], dp[i - 1][0])
                # If we swap i-th element, both arrays should be in increasing order by swapping the i-th element.
                dp[i][1] = min(dp[i][1], dp[i - 1][1] + 1)

                # If we swap i-th element, nums1[0:i] and nums2[0:i] should be in increasing order.
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                dp[i][0] = min(dp[i][0], dp[i - 1][1])
                # If we don't swap i-th element, nums1[0:i] and nums2[0:i] should be in increasing order.
                dp[i][1] = min(dp[i][1], dp[i - 1][0] + 1)

        # Minimum swaps required to make both arrays increasing, considering the last element.
        return min(dp[-1])


if __name__ == "__main__":
    nums1 = [0, 7, 8, 10, 10, 11, 12, 13, 19, 18]
    nums2 = [4, 4, 5, 7, 11, 14, 15, 16, 17, 20]
    print(f"Solution: {Solution().minSwap(nums1, nums2)}")
