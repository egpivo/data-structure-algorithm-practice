class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if(len(s) < 2 or numRows == 1):
            return s

        ans = ""
        step = 2 * (numRows - 1)

        for i in range(numRows):
            j = i
            while(j < len(s)):
                ans += s[j]

                temp = j + step - 2*i
                if (i not in [0, numRows-1]) and (temp < len(s)):
                      ans += s[temp]
                j += step

        return ans


if __name__ == "__main__":
  s = "PAYPALISHIRING"
  numRows = 3

  ans = Solution()

  print(ans.convert(s, numRows))
