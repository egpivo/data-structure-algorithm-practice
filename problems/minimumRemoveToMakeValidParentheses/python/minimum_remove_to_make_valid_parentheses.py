class Solution:
    left_parenthesis = "("
    right_parenthesis = ")"

    def minRemoveToMakeValid(self, s: str) -> str:
        """Broute force way

        Note
        ----
        - Time complexity: O(n)
        - Space complexity: O(n)
        """

        if not (self.left_parenthesis in s or self.right_parenthesis in s):
            return s

        stack = []
        collect = set()

        for index, char in enumerate(s):
            if char == "(":
                stack.append(index)
            elif char == ")":
                if stack:
                    collect.add(stack.pop())
                    collect.add(index)

        result = "".join(
            char
            for index, char in enumerate(s)
            if char not in ("(", ")") or index in collect
        )

        return result


class TowPassSolution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """2-pass

        Note
        ----
        - Time complexity: O(n)
        - Space complexity: O(n)
        """

        if not ("(" in s or ")" in s):
            return s

        # Pass 1: remove all invalid ")"
        first_pass_chars = []
        balance = 0
        open_seen = 0

        for char in s:
            if char == "(":
                balance += 1
                open_seen += 1
            if char == ")":
                if balance == 0:
                    continue
                balance -= 1

            first_pass_chars.append(char)

        # Pass 2: remove the rightmost "("
        result = []
        open_to_keep = open_seen - balance
        for char in first_pass_chars:
            if char == "(":
                open_to_keep -= 1
                if open_to_keep < 0:
                    continue
            result.append(char)

        return "".join(result)


if __name__ == "__main__":
    s = "lee(t(c)o)de)"
    print(f"Answer: {Solution().minRemoveToMakeValid(s)}")
    print(f"Answer: {TowPassSolution().minRemoveToMakeValid(s)}")
