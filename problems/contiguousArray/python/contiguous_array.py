from typing import List


class Solution:
    """

    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def findMaxLength(self, nums: List[int]) -> int:
        max_length = 0
        # Stores the count of ones encountered along with their indices
        count_dict = {0: -1}
        # Tracks the count of ones encountered so far
        one_counter = 0
        for i, num in enumerate(nums):
            if num == 0:
                one_counter -= 1
            else:
                one_counter += 1

            if one_counter in count_dict:
                max_length = max(max_length, i - count_dict[one_counter])
            else:
                count_dict[one_counter] = i

        return max_length


if __name__ == "__main__":
    nums = [0, 1, 0]

    print(f"Solution: {Solution().findMaxLength(nums)}")
