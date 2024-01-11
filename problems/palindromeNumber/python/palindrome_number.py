class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        rev = 0
        while x > rev:
            rev = 10 * rev + x % 10
            x //= 10

        return x == rev or x == rev // 10


class Solution2:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        char = str(x)
        left, right = 0, len(char) - 1

        while left < right:
            if char[left] != char[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    ans = Solution()

    x = 123
    print("input: {}".format(x))
    print("Palindrome: {}".format(ans.isPalindrome(x)))

    x = 121
    print("input: {}".format(x))
    print("Palindrome: {}".format(ans.isPalindrome(x)))
