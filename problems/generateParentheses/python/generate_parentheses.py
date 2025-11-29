from typing import List


class Solution:
    """
    Complexity
    ----------
    - Time complexity: $O(\frac{4^n}{n \cdot \sqrt(n)})$
        - `n` is the given value.
        - At each position, there are two choices (open or close), and the depth of the recursion tree is twice `n`.
        - The total number of possible combinations is $2^{2n}$.
        - However, not all combinations are valid, and the algorithm prunes certain branches early when they become invalid.
        - Estimate pruning effect: $O(\frac{1}{n \cdot \sqrt(n)})$
           - Due to the pruning conditions, some branches of the recursion tree are eliminated, leading to a reduction in the number of recursive calls.
           - This is an attempt to approximate the pruning effect on the total number of recursive calls.
           - The actual reduction in the number of recursive calls might not be precisely but the term provides a way to express the efficiency gained through pruning in terms of a square root function.
           - The goal is to capture the idea that pruning significantly reduces the search space and leads to a more efficient algorithm.
    - Space complexity: $O(n)$
        - It's due to the space required for the recursion call stack.
        - The depth of the recursion tree is proportional to the value of `n`.
    """

    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(open_count: int, close_count: int, path: List[str]) -> None:
            if len(path) == 2 * n:
                result.append("".join(path))
                return

            if open_count < n:
                path.append("(")
                backtrack(open_count + 1, close_count, path)
                path.pop()
            if close_count < open_count:
                path.append(")")
                backtrack(open_count, close_count + 1, path)
                path.pop()

        backtrack(0, 0, [])
        return result


if __name__ == "__main__":
    n = 3

    print(Solution().generateParenthesis(n))
