from typing import List


class Solution:
    """
    Note
    ----
    - TC: O(n^2)
    - SC: O(n)
    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        answer = []

        def backtrack(collection):
            if len(collection) == n:
                answer.append(collection[:])

            for i in range(n):
                if nums[i] in collection:
                    continue

                collection.append(nums[i])
                backtrack(collection[:])
                collection.pop()

        backtrack([])
        return answer


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(f"Solution is: {Solution().permute(nums)}")
