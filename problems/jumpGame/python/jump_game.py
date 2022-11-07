from typing import List


class SolutionDP:
    """
    Note
    ----
    - TC: O(n^2)
    - SC: O(n^2)
    """
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[float("inf")] * n for _ in range(n)]

        dp[0][0] = 1

        for i in range(n):
            if i + nums[i] > n - 1:
                break
            for j in range(i, i + nums[i] + 1):
                if i == j:
                    dp[i][i] = min(dp[i][:])
                else:
                    dp[j][i] = 1 + dp[i][i]

        return min(dp[-1][:])


   

if __name__ == "__main__":
  nums = [2,3,1,1,4]
  print(SolutionDP().jump(nums))

