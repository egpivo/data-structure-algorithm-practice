from typing import List


class SingleNumber:
    def single_number(self, nums: List[int]) -> int:
        once = 0
        twice = 0

        for num in nums:
            once ^= num & ~twice
            twice ^= num & ~once

        return once


if __name__ == "__main__":
    nums = [1, 2, 2, 2]
    instance = SingleNumber()

    print("Test answer")
    assert instance.single_number(nums) == 1, "Wrong Answer."
