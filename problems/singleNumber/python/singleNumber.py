from collections import Counter
from typing import List

class SingleNumber:
    def single_number(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return sorted(counter, key=counter.get, reverse=False)[0]


class SingleNumberByXOR:
    def single_number(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
          result ^= num
        return result
        

if __name__ == "__main__":
  nums = [4,1,2,1,2]
  instance = SingleNumber()
  instance_xor = SingleNumberByXOR()

  print("Test answer")
  assert instance.single_number(nums) == 4, "Wrong Answer."
  assert instance_xor.single_number(nums) == 4, "Wrong Answer."
