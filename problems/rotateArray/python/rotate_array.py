
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Complexity
        ----------
        TC: O(n)
        SC: O(1)
        """
        n = len(nums)
        k %= n

        nums[n - k:] = nums[n - k:][::-1]
        nums[:n - k] = nums[:n - k][::-1]
        nums[:] = nums[::-1]



if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    Solution().rotate(nums, k)
    print(f"Solution: {nums}")
