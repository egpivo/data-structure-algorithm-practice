from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    """

    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0

        for num in nums:
            if num != val:
                nums[count] = num
                count += 1
        return count


if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    val = 3
    print(f"k = {Solution().removeElement(nums, val)} \nnums = {nums}")
