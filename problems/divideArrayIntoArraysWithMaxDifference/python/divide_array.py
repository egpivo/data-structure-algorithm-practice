from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(nlog{n})
    - SC: O(n)
    """

    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        result = []
        nums.sort()
        n = len(nums)

        left, right = 0, 1

        while left < n:
            group = [nums[left]]

            while right < n and nums[right] - nums[left] <= k and len(group) < 3:
                group.append(nums[right])
                right += 1

            if len(group) == 3:
                result.append(group)
            else:
                return []

            left = right
            right += 1

        return result


if __name__ == "__main__":
    nums = [1, 3, 4, 8, 7, 9, 3, 5, 1]
    k = 3
    print(f"{Solution().divideArray(nums, k)}")
