from typing import List


class Solution:
    """

    Complexity
    ----------
    - TC: O(logn)
    - SC: O(1)
    """

    def __init__(self, nums: List[int]) -> None:
        self.nums = nums
        self.n = len(nums)

    def _calculate_missings(self, idx: int) -> int:
        return self.nums[idx] - self.nums[0] - idx

    def missingElement(self, k: int) -> int:

        if k > self._calculate_missings(self.n - 1):
            return nums[-1] + (k - self._calculate_missings(nums, self.n - 1))

        # binary search
        high, low = self.n - 1, 0
        while low < high:
            mid = low + (high - low) // 2
            if k > self._calculate_missings(mid):
                low = mid + 1
            else:
                high = mid

        return nums[low - 1] + (k - self._calculate_missings(low - 1))


if __name__ == "__main__":
    nums, k = [4, 7, 9, 10], 1
    print(f"{Solution(nums).missingElement(k)}")
