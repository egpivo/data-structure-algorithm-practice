from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(1)
    """

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        n = len(nums)
        count = 0
        product = 1
        left = 0

        for right in range(n):
            product *= nums[right]
            while product >= k:
                product /= nums[left]
                left += 1
            count += right - left + 1

        return count


if __name__ == "__main__":
    nums = [1, 1, 1]
    k = 2
    print(f"Solution: {Solution().numSubarrayProductLessThanK(nums, k)}")
