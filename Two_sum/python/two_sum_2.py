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
        for i, num in enumerate:
            if target - num in key:
                return [key[target - num], i]
            if num not in key:
                key[num] = i

if __name__ == '__main__':
  nums = [2, 7, 11, 15]
  print(Solution().twoSum(nums, 9))
