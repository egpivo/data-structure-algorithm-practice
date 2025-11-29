class Solution:
    """
    Complexity
    ----------
    - TC: O(1)
    - SC: O(1)
    """

    def passThePillow(self, n: int, time: int) -> int:
        loops = time // (n - 1)
        return n - time % (n - 1) if loops % 2 == 1 else 1 + time % (n - 1)


if __name__ == "__main__":
    n = 4
    time = 10
    print(f"The solution is {Solution().passThePillow(n, time)}")
