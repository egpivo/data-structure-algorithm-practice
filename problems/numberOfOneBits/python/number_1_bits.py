from typing import List


class Solution:
    
    """
    Complexity
    ----------
    - Time: O(1)
    - Space: O(1)
    """

    def hammingWeight(self, n: int) -> int:
        return sum((n & (1 << i)) != 0 for i in range(32))


if __name__ == "__main__":
    n = 11
    print(f"Solution: {Solution().hammingWeight(n)}")
