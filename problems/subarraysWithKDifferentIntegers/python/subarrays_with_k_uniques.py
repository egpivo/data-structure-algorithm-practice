from collections import defaultdict
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def count_at_most_k_distinct(nums, k):
            count = 0
            left = 0
            freqs = defaultdict(int)
            unique_count = 0

            for right, num in enumerate(nums):
                if freqs[num] == 0:
                    unique_count += 1
                freqs[num] += 1

                while unique_count > k:
                    freqs[nums[left]] -= 1
                    if freqs[nums[left]] == 0:
                        unique_count -= 1
                    left += 1

                count += right - left + 1

            return count

        return count_at_most_k_distinct(nums, k) - count_at_most_k_distinct(nums, k - 1)


if __name__ == "__main__":
    nums = [1, 2, 1, 2, 3]
    k = 2

    print(Solution().subarraysWithKDistinct(nums, k))
