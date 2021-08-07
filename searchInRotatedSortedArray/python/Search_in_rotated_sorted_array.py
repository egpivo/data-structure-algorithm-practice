class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1

        while start <= end:

            split = start + int((end - start)/2)

            if nums[split] == target:
                return split
            elif nums[split] < nums[end]:
                if (nums[split] < target) & (target <= nums[end]):
                    start = split + 1
                else:
                    end = split - 1
            else:
                if (nums[split] > target) & (target >= nums[start]):
                    end = split - 1
                else:
                    start = split + 1

        return -1





if __name__ == '__main__':

  nums = [4,5,6,7,0,1,2]
  target = 0
  ans = Solution()
  print("Output is %d" % ans.search(nums, target))

