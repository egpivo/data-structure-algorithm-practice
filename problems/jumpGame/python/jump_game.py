from typing import List


class SolutionDP:
    """
    Note
    ----
    - TC: O(n^2)
    - SC: O(n)
    """

    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n

        dp[0] = True
        for i, num in enumerate(nums):
            for j in range(i + 1, min(n, i + num + 1)):
                if dp[j - 1]:
                    dp[j] = True

            if dp[-1]:
                return True

        return dp[-1]


class SolutionGreedy:
    """
    Note
    ----
    - TC: O(n)
    - SC: O(1)
    """

    def canJump(self, nums: List[int]) -> bool:
        max_step = 0

        for num in nums[:-1]:
            max_step = max(max_step - 1, num)
            if max_step == 0:
                return False

        return True


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    print(SolutionDP().canJump(nums))
    print(SolutionGreedy().canJump(nums))
