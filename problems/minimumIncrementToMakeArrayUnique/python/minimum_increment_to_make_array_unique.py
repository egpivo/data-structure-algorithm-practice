from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n \log n)
    - SC: O(1)
    """

    def minIncrementForUnique(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        moves = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                increment = nums[i - 1] - nums[i] + 1
                nums[i] += increment
                moves += increment

        return moves


if __name__ == "__main__":
    nums = [3, 2, 1, 2, 1, 7]
    print(f"The solution is {Solution().minIncrementForUnique(nums)}")
