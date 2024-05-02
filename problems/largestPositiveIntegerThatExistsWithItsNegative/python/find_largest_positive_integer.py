from typing import List


class Solution1:
    """
    Complexity
    ----------
    - TC: O(n\log n)
    - SC: O(n)
    """

    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1

        while left < right and nums[left] < 0:
            if -nums[left] == nums[right]:
                return nums[right]
            elif -nums[left] < nums[right]:
                right -= 1
            else:
                left += 1

        return -1


class Solution2:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def findMaxK(self, nums: List[int]) -> int:
        unique_num = set(nums)
        max_k = -1

        for num in nums:
            if -num in unique_num:
                max_k = max(max_k, abs(num))

        return max_k


if __name__ == "__main__":
    nums = [-1, 10, 6, 7, -7, 1]
    print(f"The solution is {Solution1().findMaxK(nums)}")
    print(f"The solution is {Solution2().findMaxK(nums)}")
