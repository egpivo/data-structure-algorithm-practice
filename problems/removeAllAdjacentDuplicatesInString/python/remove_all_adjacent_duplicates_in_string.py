class Solution:
    """
    Complexity
    ----------
    - d: # of distinct elements
    - TC: O (n)
    - SC: O(n - d)
    """

    def removeDuplicates(self, s: str) -> str:
        stack = []

        for char in s:
            if stack and char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)


if __name__ == "__main__":
    s = "abbaca"
    print(f"{Solution().removeDuplicates(s)}")
