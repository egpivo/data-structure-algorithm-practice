from typing import List


class Solution:
    """
    Notes
    -----
    - TC: O(n)
    - SC: O(n)
    """
    _operators = ("+", "-", "*", "/")
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in self._operators:
                stack.append(int(token))
            elif token in self._operators and len(stack) >= 2:
                first = stack.pop()
                second = stack.pop()
                if token == "/":
                    calculation = int(second / first)
                elif token == "*":
                    calculation = second * first
                elif token == "+":
                    calculation = second + first
                else:
                    calculation = second - first
                stack.append(calculation)
        return stack[-1]


if __name__ == "__main__":
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(f"{Solution().evalRPN(tokens)}")
