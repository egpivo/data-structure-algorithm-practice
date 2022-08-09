import copy
from typing import List


class Solution:
    """
    Note
    ----
    - cost(i, j) = grid[i][j] + min(grid[i+1][j], grid[i][j+1])

    Complexity
    ----------
    - TC: O(nlogn)
    - SC: O(n)
    """

    def missingElement(self, nums: List[int], k: int) -> int:
        num_inner_missings = nums[-1] - nums[0] - len(nums) + 1

        if k > num_inner_missings:
            return nums[-1] + (k - num_inner_missings)

        cumsum_missings = [0] * len(nums)
        for i in range(len(nums) - 1):
            cumsum_missings[i + 1] = cumsum_missings[i] + \
                (nums[i + 1] - nums[i] - 1)

        # binary search
        high, low = len(nums) - 1, 0
        while low < high:
            mid = low + (high - low) // 2
            if cumsum_missings[mid - 1] < k <= cumsum_missings[mid]:
                return nums[mid - 1] + (k - cumsum_missings[mid - 1])

            elif k > cumsum_missings[mid]:
                low = mid + 1
            else:
                high = mid

        return nums[low] + (k - cumsum_missings[low - 1])


if __name__ == "__main__":
    nums, k = [4, 7, 9, 10], 1
    print(f"{Solution().missingElement(nums, k)}")
