from typing import List
from collections import defaultdict


class Solution:
    """
    Notes
    -----
    - TC: O(n^2)
    - SC: O(n)
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_streak = 0
        for num in nums:
            if num - 1 not in nums_set:
                count = 1
                while num + 1 in nums_set:
                    num += 1
                    count += 1
                longest_streak = max(longest_streak, count)
        return longest_streak


class Solution2:
    """
    Notes
    -----
    - TC: O(n)
    - SC: O(n)
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = defaultdict(list)
        nums_set = set(nums)

        longest_streak = 0
        for num in nums_set:
            left = right = num
            if num - 1 in lookup:
                left = lookup[num - 1][0]
            if num + 1 in lookup:
                right = lookup[num + 1][1]
            lookup[left] = [left, right]
            lookup[right] = [left, right]
            if longest_streak < right - left + 1:
                longest_streak = right - left + 1
        return longest_streak


if __name__ == "__main__":
    nums = [100,4,200,1,3,2]
    print(f"{Solution().longestConsecutive(nums)}")
    print(f"{Solution2().longestConsecutive(nums)}")
