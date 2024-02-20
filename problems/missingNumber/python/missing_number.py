from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(1)
    """

    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        max_num = -1

        for num in range(n):
            if num not in nums:
                return num

            max_num = max(max_num, num)

        return max_num + 1


class Solution2:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(1)
    """

    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        # Calculate the expected total using the correct formula for the sum of the first n natural numbers
        expected_total = (n * (n + 1)) // 2

        # Calculate the actual total by summing the elements in nums
        actual_total = sum(nums)

        # Return the difference between expected total and actual total as the missing number
        return expected_total - actual_total


if __name__ == "__main__":
    x = [3, 0, 1]
    print(f"Solution: {Solution().missingNumber(x)}")
    print(f"Solution: {Solution2().missingNumber(x)}")
