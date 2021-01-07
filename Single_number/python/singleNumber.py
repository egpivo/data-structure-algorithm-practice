from collections import Counter
from typing import List

class SingleNumber:
    def single_number(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return sorted(counter, key=counter.get, reverse=False)[0]


if __name__ == "__main__":
  nums = [4,1,2,1,2]
  instance = SingleNumber()
  print(instance.single_number(nums) == 4)
