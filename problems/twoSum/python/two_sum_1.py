"""
O(n^2)
"""
class Solution(object):
  def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in xrange(len(nums) - 1):
        for j in xrange(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


if __name__ == '__main__':
  nums = [2, 7, 11, 15]
  print(Solution().twoSum(nums, 9))
