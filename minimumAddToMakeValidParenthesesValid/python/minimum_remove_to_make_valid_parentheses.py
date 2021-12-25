class SolutionStack:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for char in s:
            if char == "(":
                stack.append(char)
            elif char == ")":
                if stack and stack[-1] == "(":
                    stack.pop(-1)
                else:
                    stack.append(char)

        return len(stack)


class SolutionCounter:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(1)
    """

    def minAddToMakeValid(self, s: str) -> int:
        invalid = 0
        left_parenthesis_count = 0

        for char in s:
            if char == "(":
                left_parenthesis_count += 1
            elif char == ")":
                if left_parenthesis_count > 0:
                    left_parenthesis_count -= 1
                else:
                    invalid += 1

        return invalid + max(left_parenthesis_count, 0)


class SolutionBalance:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(1)
    """

    def minAddToMakeValid(self, s: str) -> int:
        answer = balance = 0

        for char in s:
            balance += 1 if char == "(" else -1
            if balance == -1:
                answer += 1
                balance += 1

        return answer + balance


if __name__ == "__main__":
    s = "(()))"
    print(f"Answer: {SolutionStack().minAddToMakeValid(s)}")
    print(f"Answer: {SolutionCounter().minAddToMakeValid(s)}")
    print(f"Answer: {SolutionBalance().minAddToMakeValid(s)}")
