from typing import List


class SolutionTopDown:
    """
    Complexity
    ----------
    - TC: O(n * k)
    - SC: O(n)
    """

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [-1] * n

        def recursive(index):
            if index == n:
                return 0
            if dp[index] != -1:
                return dp[index]

            right_length = 0
            current_max = float("-inf")
            max_subarray_total = float("-inf")

            for left in range(index, min(index + k, n)):
                right_length += 1
                current_max = max(current_max, arr[left])
                max_subarray_total = max(
                    max_subarray_total, current_max * right_length + recursive(left + 1)
                )

            dp[index] = max_subarray_total
            return dp[index]

        return recursive(0)


class SolutionBottomUp:
    """
    Complexity
    ----------
    - TC: O(n * k)
    - SC: O(n)
    """

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * n

        for i in range(n):
            max_val = 0
            for j in range(1, min(i + 1, k) + 1):
                max_val = max(max_val, arr[i - j + 1])
                dp[i] = max(dp[i], (dp[i - j] if i - j > 0 else 0) + max_val * j)

        return dp[-1]


if __name__ == "__main__":
    arr = [1, 15, 7, 9, 2, 5, 10]
    k = 3
    print(f"Solution: {SolutionTopDown().maxSumAfterPartitioning(arr, k)}")
    print(f"Solution: {SolutionBottomUp().maxSumAfterPartitioning(arr, k)}")
