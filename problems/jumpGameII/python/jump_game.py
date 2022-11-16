from typing import List


class SolutionTwoDimDP:
    """
    Note
    ----
    - TC: O(n^2)
    - SC: O(n)
    """

    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[float("inf")] * n for _ in range(n)]

        dp[0][0] = 0

        for i in range(n):
            if i + nums[i] > n - 1:
                break
            for j in range(i, i + nums[i] + 1):
                if i == j:
                    dp[i][i] = min(dp[i][:])
                else:
                    dp[j][i] = 1 + dp[i][i]

        return min(dp[-1][:])


class SolutionOneDimDP:
    """
    Note
    ----
    - TC: O(n^2)
    - SC: O(n^2)
    """

    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        first_min = dp[-1]
        min_index = n - 1

        for i in range(n - 2, -1, -1):
            end = min(nums[i] + i, n - 1)
            prev_end = nums[i + 1] + i + 1
            if min_index > end or end > prev_end:
                first_min = float("inf")

                for j in range(i + 1, end + 1):
                    if dp[j] < first_min:
                        first_min = dp[j]
                        min_index = j
            dp[i] = float("inf") if nums[i] == 0 else first_min + 1
        return dp[0]


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    print(SolutionTwoDimDP().jump(nums))
    print(SolutionOneDimDP().jump(nums))
