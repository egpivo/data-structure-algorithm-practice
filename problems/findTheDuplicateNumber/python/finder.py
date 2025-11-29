from typing import List


class Solution:
    """
    Complexity
    ----------
    - Time complexity: O(n)
    - Space complexity: O(1)
    """

    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        # Phase 1: Find the intersection point of the two pointers
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # Reset one pointer to the beginning and move both pointers at the same pace
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


if __name__ == "__main__":
    nums = [1, 3, 4, 2, 2]
    print(f"The solution is {Solution().findDuplicate(nums)}")
