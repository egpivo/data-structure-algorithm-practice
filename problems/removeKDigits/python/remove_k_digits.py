from collections import deque


class Solution:
    """
    Complexity
    ----------
    - TC: O(n + k)
    - SC: O(n)
    """

    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return "0"

        stack = deque()
        removed = 0

        for digit in num:
            while stack and removed < k and stack[-1] > digit:
                stack.pop()
                removed += 1
            stack.append(digit)
        # If there are remaining elements to be removed, remove them from the end
        while removed < k:
            stack.pop()
            removed += 1

        # Remove leading zeros
        while stack and stack[0] == "0":
            stack.popleft()

        return "".join(stack) if stack else "0"


if __name__ == "__main__":
    num = "1432219"
    k = 3
    print(f"Solution = {Solution().removeKdigits(num, k)}")
