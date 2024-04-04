class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(1)
    """

    def maxDepth(self, s: str) -> int:
        max_depth = 0
        depth = 0
        for char in s:
            if char == "(":
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ")":
                depth -= 1
        return max_depth


if __name__ == "__main__":
    s = "(1+(2*3)+((8)/4))+1"
    print(f"The solution is {Solution().maxDepth(s)}")
