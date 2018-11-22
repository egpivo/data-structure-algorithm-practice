class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n < 2: return s

        start = end = 0

        for i in range(n-1):
          start, end = self.searchPalindrome(s, i, i, start, end)
          start, end = self.searchPalindrome(s, i, i + 1, start, end)

        return s[start:(start+end)]


    def searchPalindrome(self, s, left, right, start, end):

        while(left >= 0) and (right < len(s)) and (s[left] == s[right]):
            left -= 1
            right += 1

        if(end < right - left - 1):
            start = left + 1
            end = right - left - 1

        return start, end


if __name__ == "__main__":
  s = "babad"

  ans = Solution()
  print("Palindromic substing is: " + ans.longestPalindrome(s))
