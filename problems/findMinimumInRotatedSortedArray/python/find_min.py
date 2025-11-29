from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        change_point = self.find_change_point(nums)
        if change_point >= len(nums):
            return nums[0]
        return min(nums[change_point], nums[0])

    def find_change_point(self, nums):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                return mid + 1
            else:
                if nums[mid] < nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
        return left


if __name__ == "__main__":
    nums = [3, 4, 5, 1, 2]
    print(f"Solution: {Solution().findMin(nums)}")
