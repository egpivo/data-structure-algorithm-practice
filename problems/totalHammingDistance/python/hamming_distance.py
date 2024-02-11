from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(1)
    """

    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            zeros = ones = 0
            mask = 1 << i
            for num in nums:
                if mask & num:
                    ones += 1
                else:
                    zeros += 1
            ans += ones * zeros
        return ans


if __name__ == "__main__":
    nums = [4, 14, 2]
    print(f"Solution: {Solution().totalHammingDistance(nums)}")
