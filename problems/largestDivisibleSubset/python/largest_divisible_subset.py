from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        if n == 0:
            return []

        dp = [1] * n
        prev = [-1] * n
        max_len, max_index = 1, 0

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j

            if dp[i] > max_len:
                max_len = dp[i]
                max_index = i

        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = prev[max_index]

        return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(f"The solution is {Solution().largestDivisibleSubset(nums)}")
