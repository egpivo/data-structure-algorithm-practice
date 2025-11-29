from collections import Counter
from typing import List


class SingleNumber:
    def single_number(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return sorted(counter, key=counter.get, reverse=False)[0]


class SingleNumberByXOR:
    """
    Notes
    -----
    -   a ^ a = 0 for any number a, and 0 ^ a = a

    Examples
    --------
    - Initialization: result = 4 (first element in the array)
    - Iteration:
        result ^= 2 (4 ^ 2 = 6)
          - In binary, 4 is 100 and 2 is 010. The XOR of these two binary numbers is 110, which is 6 in decimal.
        result ^= 3 (6 ^ 3 = 5)
          -  In binary, 6 is 110 and 3 is 011. The XOR of these two binary numbers is 101, which is 5 in decimal.
        result ^= 2 (5 ^ 2 = 7)
          -  In binary, 5 is 101 and 2 is 010. The XOR of these two binary numbers is 111, which is 7 in decimal.
        result ^= 4 (7 ^ 4 = 3)
          - In binary, 7 is 111 and 4 is 100. The XOR of these two binary numbers is 011, which is 3 in decimal.
    """

    def single_number(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


if __name__ == "__main__":
    nums = [4, 1, 2, 1, 2]
    instance = SingleNumber()
    instance_xor = SingleNumberByXOR()

    print("Test answer")
    assert instance.single_number(nums) == 4, "Wrong Answer."
    assert instance_xor.single_number(nums) == 4, "Wrong Answer."
