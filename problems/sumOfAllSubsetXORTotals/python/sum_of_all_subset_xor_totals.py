from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(2^n)
    - SC: O(n)
    """

    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(index, current_xor):
            if index == len(nums):
                return current_xor

            # Include the current element in the subset
            with_current = backtrack(index + 1, current_xor ^ nums[index])
            # Exclude the current element from the subset
            without_current = backtrack(index + 1, current_xor)

            # Return the sum of both cases
            return with_current + without_current

        # Start backtracking from index 0 and initial XOR value of 0
        return backtrack(0, 0)


if __name__ == "__main__":
    nums = [5, 1, 6]

    print(Solution().subsetXORSum(nums))
