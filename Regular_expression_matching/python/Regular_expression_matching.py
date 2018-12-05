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


## Dynamic Programming
class Solution2:
    def isMatch(self, s, p):
        """
            :type s: str
            :type p: str
            :rtype: bool
            """
        
        dp = [[False] * (len(p) + 1 ) for _ in range(len(s) + 1) ]
        dp[-1][-1] = True # for the last element is matched

        for i in range(len(s), -1, -1): # the first loop is for '*'
            for j in range(len(p) - 1, -1, -1):
                scan = i < len(s) and p[j] in [s[i], '.']
    
                if j + 1 < len(p) and p[j + 1] == '*':
                    dp[i][j] = dp[i][j+2] or (scan and dp[i+1][j])
                
                elif i < len(s):
                    dp[i][j] = scan and dp[i+1][j+1]
        

        return dp[0][0]


if __name__ == "__main__":
  s = "aaacbg"
  p = "a*cb."

  ans = Solution()

  print("Input: s={}, p={}".format(s, p))
  print("Output: {}".format(ans.isMatch(s,p)))

  ans = Solution2()

  print("Input: s={}, p={}".format(s, p))
  print("Output: {}".format(ans.isMatch(s,p)))



