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

class SolutionBalance:
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

if __name__ == "__main__":
    s = "lee(t(c)o)de)"
    print(f"Answer: {SolutionStack().minAddToMakeValid(s)}")
    print(f"Answer: {SolutionBalance().minAddToMakeValid(s)}")