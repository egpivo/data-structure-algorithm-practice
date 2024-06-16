from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(m + log(n))
    - SC: O(1)
    """

    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1
        i = patches = 0

        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss *= 2
                patches += 1

        return patches


if __name__ == "__main__":
    nums = [1, 3]
    n = 6
    print(f"The solution is {Solution().minPatches(nums,n)}")
