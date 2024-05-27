from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n\log n)
    - SC: O(1)
    """

    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse=True)
        for x in range(1, n + 1):
            if nums[x - 1] >= x:
                if x == n or nums[x] < x:
                    return x
        return -1


if __name__ == "__main__":
    nums = [3, 5]
    print(f"The solution is {Solution().specialArray(nums)}")
