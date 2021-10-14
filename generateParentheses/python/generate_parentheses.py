from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(parenthese = [], left = 0, right = 0):
            if len(parenthese) == 2 * n:
                ans.append("".join(parenthese))
                return

            if left < n:
                parenthese.append("(")
                backtrack(parenthese, left + 1, right)
                parenthese.pop()
             
            if right < left:
                parenthese.append(")")
                backtrack(parenthese, left, right + 1)
                parenthese.pop()

        backtrack()
        return ans


if __name__ == "__main__":
  n = 3

  print(Solution().generateParenthesis(n))
