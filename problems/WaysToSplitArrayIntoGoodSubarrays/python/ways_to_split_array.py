from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        # Find indices of 1's
        one_indices = [i for i, num in enumerate(nums) if num == 1]

        if not one_indices:
            return 0

        modulo = 10**9 + 7
        result = 1

        for i in range(1, len(one_indices)):
            result *= one_indices[i] - one_indices[i - 1]
            result %= modulo

        return result


if __name__ == "__main__":
    nums = [1, 0, 1, 0, 1]
    print(f"The solution is {Solution().numberOfGoodSubarraySplits(nums)}")
