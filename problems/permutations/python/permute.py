from typing import List


class Solution:
    """
    Note
    ----
    -  Time complexity: $O(n!)$
        - The time complexity is factorial as each recursive call explores all possible arrangements.
    - Space complexity: $O(n)$
        - The space complexity is linear as the depth of the recursion is limited by the length of the input list (`nums`), and additional space is used for the result list and the current path.
    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        answer = []

        def backtrack(collection):
            if len(collection) == n:
                answer.append(collection[:])

            for i in range(n):
                if nums[i] not in collection:
                    collection.append(nums[i])
                    backtrack(collection)
                    collection.pop()

        backtrack([])
        return answer


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(f"Solution is: {Solution().permute(nums)}")
