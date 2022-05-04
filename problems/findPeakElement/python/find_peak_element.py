from typing import List


class SolutionIterative:
    """

    Complexity
    ----------
    - TC: O(log_2 n)
    - SC: O(1)
    """

    def findPeakElement(self, nums: List[int]) -> int:
        len_nums = len(nums)
        left, right = 0, len_nums - 1

        while left <= right:
            mid = left + (right - left) // 2
            if mid + 1 < len_nums and nums[mid] <= nums[mid + 1]:
                left = mid + 1
            elif mid - 1 >= 0 and nums[mid] < nums[mid - 1]:
                right = mid - 1
            else:
                return mid


class SolutionRecursive:
    """

    Complexity
    ----------
    - TC: O(log_2 n)
    - SC: O(log_2 n)
    """

    def findPeakElement(self, nums: List[int]) -> int:
        return self._recurse(nums, 0, len(nums) - 1)

    def _recurse(self, nums: List[int], left: int, right: int) -> int:
        if left == right:
            return left
        mid = left + (right - left) // 2
        if nums[mid] > nums[mid + 1]:
            return self._recurse(nums, left, mid)
        return self._recurse(nums, mid + 1, right)


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(f"Solution: {SolutionIterative().findPeakElement(nums)}")
    print(f"Solution: {SolutionRecursive().findPeakElement(nums)}")
