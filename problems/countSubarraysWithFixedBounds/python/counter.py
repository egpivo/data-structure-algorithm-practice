from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(1)
    """

    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        left = -1
        prev_minK_index = -1
        prev_maxK_index = -1

        for right, num in enumerate(nums):
            if not (minK <= num <= maxK):
                left = right
            else:
                if num == minK:
                    prev_minK_index = right
                if num == maxK:
                    prev_maxK_index = right

            count += max(0, min(prev_minK_index, prev_maxK_index) - left)

        return count


if __name__ == "__main__":
    nums = [1, 3, 5, 2, 7, 5]
    minK = 1
    maxK = 5

    print(Solution().countSubarrays(nums, minK, maxK))
