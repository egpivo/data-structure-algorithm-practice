from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def backtrack(open_count, close_count, path):
            if len(path) == 2 * n:
                answer.append("".join(path))
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
        return answer


if __name__ == "__main__":
    n = 3

    print(Solution().generateParenthesis(n))
