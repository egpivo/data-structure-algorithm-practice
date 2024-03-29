from typing import List


class Solution:
    """

    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map = {0: -1}
        total = 0

        for idx, num in enumerate(nums):
            total += num
            total %= k

            if total not in remainder_map:
                remainder_map[total] = idx
            else:
                if idx - remainder_map[total] > 1:
                    return True

        return False


class Solution2:
    """

    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        nums[0] %= k
        seen_remainders = {0}

        for i in range(1, len(nums)):
            nums[i] = (nums[i] + nums[i - 1]) % k
            if nums[i] in seen_remainders:
                return True
            seen_remainders.add(nums[i - 1])
        return False


if __name__ == "__main__":
    nums = [23, 2, 6, 4, 7]

    print(f"Solution: {Solution().checkSubarraySum(nums, 6)}")
    print(f"Solution: {Solution().checkSubarraySum(nums, 9)}")

    print(f"Solution: {Solution2().checkSubarraySum(nums, 6)}")
    print(f"Solution: {Solution2().checkSubarraySum(nums, 9)}")
