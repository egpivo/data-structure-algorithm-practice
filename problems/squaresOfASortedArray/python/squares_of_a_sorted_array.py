from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(N)
    - SC: O(N)
    """

    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1

        answer = []
        while 0 <= left <= right < len(nums):
            if abs(nums[left]) < abs(nums[right]):
                answer.append(nums[right] ** 2)
                right -= 1
            else:
                answer.append(nums[left] ** 2)
                left += 1
        return answer[::-1]


class Solution2:
    """
    Complexity
    ----------
    - TC: O(N)
    - SC: O(N)
    """

    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Find the index where positive numbers start
        right = next((i for i, num in enumerate(nums) if num > 0), n)

        left = right - 1
        result = []

        # Merge the squared values of the left and right pointers
        while left >= 0 and right < n:
            left_squared, right_squared = nums[left] ** 2, nums[right] ** 2
            if left_squared < right_squared:
                result.append(left_squared)
                left -= 1
            else:
                result.append(right_squared)
                right += 1

        # Add remaining squared values from the left pointer
        result.extend(nums[left] ** 2 for left in range(left, -1, -1))

        # Add remaining squared values from the right pointer
        result.extend(nums[right] ** 2 for right in range(right, n))

        return result


if __name__ == "__main__":
    nums = [-4, -1, 0, 3, 10]
    print(f"{Solution().sortedSquares(nums)}")
    print(f"{Solution2().sortedSquares(nums)}")
