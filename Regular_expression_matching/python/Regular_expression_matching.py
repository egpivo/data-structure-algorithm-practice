class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p: return not s

        if len(p) > 1 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (s != "" and (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p))

        else:
            return s != "" and (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])


if __name__ == "__main__":
  s = "aaa"
  p = "a*"

  ans = Solution()

  print("Input: s={}, p={}".format(s, p))
  print("Output: {}".format(ans.isMatch(s,p)))
