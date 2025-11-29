class Solution:
    """
    Complexity
    ----------
    - TC: O(log n)
    - SC: O(1)
    """

    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        digit_sum = 0
        copy_x = x

        while copy_x > 0:
            digit_sum += copy_x % 10
            copy_x //= 10

        return digit_sum if x % digit_sum == 0 else -1


if __name__ == "__main__":
    num = 101
    print(f"The solution is {Solution().sumOfTheDigitsOfHarshadNumber(num)}")
