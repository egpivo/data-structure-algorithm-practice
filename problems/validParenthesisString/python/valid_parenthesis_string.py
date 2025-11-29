class Solution1:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(1)
    """

    def checkValidString(self, s: str) -> bool:
        min_open = max_open = 0

        for char in s:
            if char == "(":
                min_open += 1
                max_open += 1
            elif char == ")":
                if min_open > 0:
                    min_open -= 1
                max_open -= 1
            else:  # char == "*"
                if min_open > 0:
                    min_open -= 1
                max_open += 1

            if (
                max_open < 0
            ):  # If max_open becomes negative, it means too many ')' encountered
                return False

        return min_open == 0  # If min_open is not 0, it means there are unmatched '('


class Solution2:
    def checkValidString(self, s: str) -> bool:
        left_stack = []
        star_stack = []

        for i, char in enumerate(s):
            if char == "(":
                left_stack.append(i)
            elif char == "*":
                star_stack.append(i)
            elif char == ")":
                # Attempt to match ')' with '(' from left_stack or '*' from star_stack
                if left_stack:
                    left_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False

        # Matching remaining '(' in left_stack with '*' in star_stack
        while left_stack and star_stack:
            if left_stack[-1] < star_stack[-1]:
                left_stack.pop()
                star_stack.pop()
            else:
                break

        # If left_stack is empty, it means all '(' are matched by either ')' or '*'
        return not left_stack


if __name__ == "__main__":
    s = "(*))"
    print(f"Answer: {Solution1().checkValidString(s)}")
    print(f"Answer: {Solution2().checkValidString(s)}")
