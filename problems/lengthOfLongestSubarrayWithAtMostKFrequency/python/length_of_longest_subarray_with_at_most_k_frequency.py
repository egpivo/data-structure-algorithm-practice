from collections import defaultdict
from typing import List


class Solution:
    """
    Complexity
    ----------
    - Time complexity: O(n)
    - Space complexity: O(n)
    """

    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freqs = defaultdict(int)
        max_length = 0

        left = 0

        for right, num in enumerate(nums):
            freqs[num] += 1

            while freqs[num] > k and left <= right:
                freqs[nums[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length


if __name__ == "__main__":
    nums = [1, 2, 3, 1, 2, 3, 1, 2]
    k = 2

    print(f"Solution: {Solution().maxSubarrayLength(nums, k)}")
