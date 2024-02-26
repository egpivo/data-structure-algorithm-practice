from typing import List


class Solution1:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(1)
    """

    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_product = -float("inf")
        prefix = suffix = 1

        for i in range(n):
            prefix *= nums[i]
            max_product = max(max_product, prefix)
            prefix = 1 if prefix == 0 else prefix

        suffix = 1
        for i in range(n - 1, -1, -1):
            suffix *= nums[i]
            max_product = max(max_product, suffix)
            suffix = 1 if suffix == 0 else suffix

        return max_product


class Solution2:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        max_product = nums[0]
        min_product = nums[0]
        result = max_product

        for i in range(1, n):
            if nums[i] < 0:
                max_product, min_product = min_product, max_product

            max_product = max(nums[i], max_product * nums[i])
            min_product = min(nums[i], min_product * nums[i])

            result = max(result, max_product)

        return result


if __name__ == "__main__":
    nums = [2, 3, -2, 4]
    print(f"Solution: {Solution1().maxProduct(nums)}")
    print(f"Solution2: {Solution2().maxProduct(nums)}")
