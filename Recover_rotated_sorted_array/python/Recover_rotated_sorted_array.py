class Solution:
    """
    @param: nums: An integer array
    @return: nothing
    """

    def reverse(self, nums, start, end):

        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def recoverRotatedSortedArray(self, nums):

        if(len(nums) <= 1):
            return
        for i in range(len(nums) - 1):
            if(nums[i] > nums[i+1]):
                self.reverse(nums, 0, i)
                print(nums)
                self.reverse(nums, i + 1, len(nums) - 1)
                print(nums)
                self.reverse(nums, 0, len(nums) - 1)
                print(nums)




if __name__ == '__main__':

    nums = [4, 5, 6, 7, 1, 2, 3]
    ans = Solution()
    _ = ans.recoverRotatedSortedArray(nums)
    print(nums)
