class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        ans = 0
        while x != 0:
          ans = ans * 10 + abs(x) % 10 * ((x >= 0)-(x < 0))
          x = int(x / 10)

        return ans if (abs(ans) <= (2 ** 31 - 1)) else 0




if __name__ == "__main__":
    x = 123
    ans = Solution()

    print("The input: {}; the output: {}".format(x, ans.reverse(x)))
