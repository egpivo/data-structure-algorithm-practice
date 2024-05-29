class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(1)
    """

    def numSteps(self, s: str) -> int:
        steps = 0
        num = int(s, 2)

        while num != 1:
            if num % 2 == 0:
                num >>= 1
            else:
                num += 1
            steps += 1

        return steps


if __name__ == "__main__":
    s = "1101"
    print(f"The solution is {Solution().numSteps(s)}")
