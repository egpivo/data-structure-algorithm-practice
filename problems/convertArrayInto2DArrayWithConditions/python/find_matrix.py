from collections import Counter
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        result = []
        while nums:
            collection = []
            size = len(nums)
            for _ in range(size):
                value = nums.pop(0)
                if value not in collection:
                    collection.append(value)
                else:
                    nums.append(value)
            result.append(collection)
        return result


class Solution2:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        num_count = Counter(nums)

        result = [[] for _ in range(max(num_count.values()))]

        for num, freq in num_count.items():
            for i in range(freq):
                result[i].append(num)

        return result


if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9, 5, -10, -3, -3, 9, 5]
    print(f"The answer is {Solution().findMatrix(nums)}")
    nums = [-10, -3, 0, 5, 9, 5, -10, -3, -3, 9, 5]
    print(f"The answer is {Solution2().findMatrix(nums)}")
