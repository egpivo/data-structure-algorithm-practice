class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str: return 0

        ans = 0
        sign = 1
        INT_MAX = 2 ** 31 -1 # 2147483647
        INT_MIN = - 2 ** 31

        if(str[0] == '+' or str[0] == '-'):
            sign = 1 if str[0] == '+' else -1
            str = str[1:]
        idx = 0

        while(idx < len(str) and str[idx] >= '0' and str[idx] <= '9'):

            if(ans > INT_MAX/10 or (ans == 214748364 and str[idx] > '7')):
                return INT_MAX if sign == 1 else INT_MIN
            ans = ans*10 + ord(str[idx]) - ord('0')
            idx += 1

        return sign*ans

if __name__ == "__main__":
  str = "4193 with words"
  ans = Solution()

  print("Input: {}".format(str))
  print("Output: {}".format(ans.myAtoi(str)))
