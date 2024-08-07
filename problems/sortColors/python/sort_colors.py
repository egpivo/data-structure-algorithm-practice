from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(1)
    """

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        current = 0

        while current <= right:
            if nums[current] == 0:
                nums[current], nums[left] = nums[left], nums[current]
                left += 1
                current += 1
            elif nums[current] == 2:
                nums[current], nums[right] = nums[right], nums[current]
                right -= 1
            else:
                current += 1


if __name__ == "__main__":
    input = [2, 0, 2, 1, 1, 0]
    answer = Solution().sortColors(input)
    print(input)
