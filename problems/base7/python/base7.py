class Solution:
    """
        Complexity
    ----------
    - p: the power of 7 which is the closest to num
    - TC: O(p)
    - SC: O(1)
    """

    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        remainder = num % 7
        abs_num = abs(num // 7)
        power = 1
        while abs_num:
            remainder += (abs_num % 7) * 10**power
            power += 1
            abs_num //= 7

        return str(remainder) if num > 0 else "-" + str(remainder)


class Solution2:
    """
    Complexity
    ----------
    - p: the power of 7 which is the closest to num
    - TC: O(p)
    - SC: O(p)
    """

    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        sign = "-" if num < 0 else ""
        remainders = []
        abs_num = abs(num)
        while abs_num:
            remainders.append(str(abs_num % 7))
            abs_num //= 7
        remainders.append(sign)
        return "".join(reversed(remainders))


if __name__ == "__main__":
    num = 101
    print(f"The solution is {Solution().convertToBase7(num)}")
    print(f"The solution is {Solution2().convertToBase7(num)}")
