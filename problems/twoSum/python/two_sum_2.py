"""
apply Hashmap
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        key = {}
        for i, num in enumerate(nums):
            if target - num in key:
                return [key[target - num], i]
            if num not in key:
                key[num] = i


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return left + 1, right + 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return [None, None]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    print(Solution().twoSum(nums, 9))
