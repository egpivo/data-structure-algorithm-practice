from typing import List

class SolutionDP:
    def maxSubArray(self, nums: List[int]) -> int:

        """
        Complexity
        ----------
        TC: O(n)
        SC: O(n)
        """
        n = len(nums)
        dp = [0] * n

        for i in range(n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        """
        Complexity
        ----------
        TC: O(n)
        SC: O(1)
        """

        answer = 0
        current_maximum = 0
        for num in nums:
            current_maximum = max(current_maximum + num, num)
            answer = max(answer, current_maximum)

        return answer
        

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(f"Solution: {Solution().maxSubArray(nums)}")
    print(f"Solution: {SolutionDP().maxSubArray(nums)}")
