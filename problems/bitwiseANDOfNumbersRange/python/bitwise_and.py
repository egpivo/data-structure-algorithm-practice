class Solution:
    """
    Complexity
    ----------
    - TC: O(log(max(left, right))
    - SC: O(1)
    """

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift


if __name__ == "__main__":
    print(f"The solution is {Solution().rangeBitwiseAnd(4, 5)}")
