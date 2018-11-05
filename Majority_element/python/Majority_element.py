class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in set(nums):
            if nums.count(i) >= len(nums)/2:
                return i

        return -1


if __name__ == "__main__":
  nums = [2,2,1,1,1,2,2]
  ans = Solution()
  print(ans.majorityElement(nums))
