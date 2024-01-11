from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = 1

        for i in range(len(digits) - 1, -1, -1):
            digit += digits[i]
            if digit >= 10:
                digits[i] = digit % 10
                digit //= 10
            else:
                digits[i] = digit
                digit = 0
                break
        if digit > 0:
            digits = [digit] + digits
        return digits


if __name__ == "__main__":
    ans = Solution()

    digits = [1, 2, 3]
    print(f"input: {digits}")
    print("Palindrome: {}".format(ans.plusOne(digits)))

    digits = [9]
    print(f"input: {digits}")
    print("Palindrome: {}".format(ans.plusOne(digits)))
