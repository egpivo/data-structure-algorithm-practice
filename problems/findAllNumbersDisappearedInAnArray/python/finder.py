from typing import List


class Solution:
    """
    - Time complexity: O(n)
    - Space complexity: O(1)
    """

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            while nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        return [i + 1 for i in range(n) if i + 1 != nums[i]]


class Solution2:
    """
    - Time complexity: O(n)
    - Space complexity: O(1)
    """

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        len(nums)
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])

        return [i + 1 for i, num in enumerate(nums) if num > 0]


if __name__ == "__main__":
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(f"Solution: {Solution().findDisappearedNumbers(nums)}")
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(f"Solution2: {Solution2().findDisappearedNumbers(nums)}")
