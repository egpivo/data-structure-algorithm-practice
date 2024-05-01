from typing import List


class Solution:
    """
    Complexity
    ----------
    - SC: O(n)
    - TC: O(1)
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        left, right = 0, 1

        while right < len(nums):
            if nums[left] != nums[right]:
                nums[count] = nums[right]
                left = right
                count += 1
            left = right
            right += 1

        return count


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    print(f"{Solution().removeDuplicates(nums)} \nnums = {nums}")
