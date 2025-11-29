from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(1)
    """

    def minOperations(self, nums: List[int], k: int) -> int:
        xor_result = k
        for num in nums:
            xor_result ^= num
        return bin(xor_result).count("1")


if __name__ == "__main__":
    nums = [2, 1, 3, 4]
    k = 1
    print(f"The Solution is {Solution().minOperations(nums, k)}")
