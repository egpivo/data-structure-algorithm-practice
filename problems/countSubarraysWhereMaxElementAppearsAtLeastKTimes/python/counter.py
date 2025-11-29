from collections import deque
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(1)
    """

    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_value = max(nums)
        max_value_indices = deque()
        total_subarrays = 0
        start_index = -1

        for end_index, num in enumerate(nums):
            if num == max_value:
                max_value_indices.append(end_index)

                if len(max_value_indices) == k:
                    next_start_index = max_value_indices.popleft()
                    remaining_subarrays = n - end_index
                    valid_subarrays_from_start = next_start_index - start_index
                    total_subarrays += remaining_subarrays * valid_subarrays_from_start
                    start_index = next_start_index

        return total_subarrays


if __name__ == "__main__":
    nums = [1, 3, 2, 3, 3]
    k = 2

    print(f"Solution: {Solution().countSubarrays(nums, k)}")
