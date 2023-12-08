from typing import List


class SolutionTwoPointers:
    """
    Complexity
    ----------
    TC: O(n^2)
    SC: O(log n) /O(n) (depending on sorting)
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        nums.sort()
        res = []
        for idx, num in enumerate(nums):
            if num > 0:
                break
            if idx == 0 or nums[idx - 1] != num:
                self.twoSum(nums, idx, res)
        return res

    def twoSum(self, nums, idx, res):
        left, right = idx + 1, len(nums) - 1

        while left < right:
            total = nums[idx] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                res.append([nums[left], nums[idx], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left - 1] == nums[left]:
                    left += 1


class SolutionNotSorting:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        dups = set()
        seen = {}

        for idx, num in enumerate(nums):
            if num not in dups:
                dups.add(num)
                for num2 in nums[idx + 1 :]:
                    complement = -num - num2
                    if complement in seen and seen[complement] == idx:
                        res.add(tuple(sorted([num, num2, complement])))
                    seen[num2] = idx
        return res


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(SolutionTwoPointers().threeSum(nums))
    print(SolutionNotSorting().threeSum(nums))
