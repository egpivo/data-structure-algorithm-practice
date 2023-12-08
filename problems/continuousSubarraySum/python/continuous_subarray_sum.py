from typing import List


class Solution:
    """

    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map = {0: -1}
        total = 0

        for idx, num in enumerate(nums):
            total += num
            total %= k

            if total not in remainder_map:
                remainder_map[total] = idx
            else:
                if idx - remainder_map[total] > 1:
                    return True

        return False


if __name__ == "__main__":
    nums = [23, 2, 6, 4, 7]

    print(f"Solution: {Solution().checkSubarraySum(nums, 6)}")
    print(f"Solution: {Solution().checkSubarraySum(nums, 9)}")
