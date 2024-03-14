from collections import defaultdict
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cum_sum = 0
        result = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1

        for num in nums:
            cum_sum += num
            result += prefix_sum[cum_sum - goal]
            prefix_sum[cum_sum] += 1

        return result


if __name__ == "__main__":
    nums = [1, 0, 1, 0, 1]
    goal = 2
    print(f"The solution is {Solution().numSubarraysWithSum(nums, goal)}")
