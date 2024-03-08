from collections import Counter
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # Count the frequency of each element in the list
        frequencies = list(Counter(nums).values())

        # Find the maximum frequency among the elements
        max_freq = max(frequencies)

        # Count the number of elements with the maximum frequency
        num_elements_with_max_freq = frequencies.count(max_freq)

        # Calculate the product of the maximum frequency and the count of elements with that frequency
        result = num_elements_with_max_freq * max_freq

        return result


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(f"The solution is {Solution().maxFrequencyElements(nums)}")
