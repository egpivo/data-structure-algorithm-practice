from typing import List


class Solution:
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


if __name__ == "__main__":
    nums = [100,4,200,1,3,2]
    print(f"{Solution().longestConsecutive(nums)}")
