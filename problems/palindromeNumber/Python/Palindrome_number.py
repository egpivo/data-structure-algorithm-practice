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


if __name__ == "__main__":
    ans = Solution()

    x = 123
    print("input: {}".format(x))
    print("Palindrome: {}".format(ans.isPalindrome(x)))

    x = 121
    print("input: {}".format(x))
    print("Palindrome: {}".format(ans.isPalindrome(x)))
