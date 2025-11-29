from collections import Counter
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def singleNumber(self, nums: List[int]) -> List[int]:
        return [num for num, count in Counter(nums).items() if count == 1]


class Solution2:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(1)
    """

    def singleNumber(self, nums: List[int]) -> List[int]:
        # Step 1: XOR all numbers to find the XOR of the two unique numbers
        xor_result = 0
        for num in nums:
            xor_result ^= num

        # Step 2: Find a set bit in xor_result (we use the rightmost set bit)
        set_bit = xor_result & -xor_result

        # Step 3: Partition numbers into two groups and XOR them separately
        num1, num2 = 0, 0
        for num in nums:
            if num & set_bit:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]


if __name__ == "__main__":
    nums = [1, 2, 1, 3, 2, 5]
    print(f"The solution is {Solution().singleNumber(nums)}")
    print(f"The solution is {Solution2().singleNumber(nums)}")
