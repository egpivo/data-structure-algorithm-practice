class Solution:
    def search(self, nums, target):
        """
        Complexity
        ----------
        TC: O(logN)
        SC: O(1)
        """
        start = 0
        end = len(nums) - 1

        while start <= end:
            split = start + (end - start) // 2

            if nums[split] == target:
                return split
            elif nums[split] < nums[end]:
                if nums[split] < target <= nums[end]:
                    start = split + 1
                else:
                    end = split - 1
            else:
                if nums[split] > target >= nums[start]:
                    end = split - 1
                else:
                    start = split + 1

        return -1


class Solution2:
    def search(self, nums, target):
        """
        Complexity
        ----------
        TC: O(logN)
        SC: O(1)
        """
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1

        rotated_index = self.find_rotated_index(nums, 0, n - 1)
        if nums[rotated_index] == target:
            return rotated_index
        if rotated_index == 0:
            return self.binary_search(nums, target, 0, n - 1)
        elif target < nums[0]:
            return self.binary_search(nums, target, rotated_index, n - 1)
        else:
            return self.binary_search(nums, target, 0, rotated_index)

    def find_rotated_index(self, nums, left, right):
        while left <= right:
            mid = left + (right - left) // 2
            if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                return mid + 1
            else:
                if nums[mid] < nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
        return 0

    def binary_search(self, nums, target, left, right):
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1


if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    ans = Solution()
    print("Output is %d" % ans.search(nums, target))
    print("Output is %d" % Solution2().search(nums, target))
