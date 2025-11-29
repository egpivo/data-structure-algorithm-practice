from typing import List


class Solution:
    """
    - Time complexity: O(n)
    - Space complexity: O(1)
    """

    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            if not 0 < nums[i] <= n:
                nums[i] = n + 1

        for i in range(n):
            index = abs(nums[i])
            if 0 < index <= n:
                nums[index - 1] = -abs(nums[index - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1


class Solution2:
    """
    - Time complexity: O(n)
    - Space complexity: O(1)
    """

    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Step 1: Mark the presence of each positive number by changing the sign of nums[num - 1]
        for i, num in enumerate(nums):
            while 1 <= num <= n and nums[num - 1] != num:
                nums[num - 1], nums[i] = nums[i], nums[num - 1]
                num = nums[i]
        # Step 2: Find the first index where nums[index] != index + 1, indicating the missing positive integer
        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1

        # If all positive integers from 1 to n are present, return n + 1
        return n + 1


if __name__ == "__main__":
    nums = [3, 4, -1, 1]
    print(f"Solution: {Solution().firstMissingPositive(nums)}")
    nums = [3, 4, -1, 1]
    print(f"Solution2: {Solution2().firstMissingPositive(nums)}")
