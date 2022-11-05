from typing import List


class Solution:
    """
    Note
    ----
    - Time Complexity: O(log n)
    - Space Complexity: O(1)
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lower_bound = self.binary_search(nums, target, True)
        if lower_bound == -1:
            return [-1, -1]
        upper_bound = self.binary_search(nums, target, False)
        return [lower_bound, upper_bound]

    def binary_search(self, nums: List[int], target: int, is_lower_bound: bool) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                if is_lower_bound:
                    if mid == left or nums[mid - 1] < target:
                        return mid
                    right = mid - 1
                else:
                    if mid == right or nums[mid + 1] > target:
                        return mid
                    left = mid + 1                    

            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
        

if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    target = 8
    print(f"Solution: {Solution().searchRange(nums, target)}")
