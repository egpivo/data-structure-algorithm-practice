class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        temp = {}
        ans = 0
        idx = -1

        for i, char in enumerate(s):
          idx = max(idx, temp.get(char, -1))
          temp[char] = i
          ans = max(ans, i - idx)

        return ans


if __name__ == '__main__':
  test1 = "abcabcbb"
  test2 = "bbbbb"
  test3 = "pwwkew"

  detect = Solution()
  print("Given %s  the length is %d"% (test1, detect.lengthOfLongestSubstring(test1)))
  print("Given %s  the length is %d"% (test2, detect.lengthOfLongestSubstring(test2)))
  print("Given %s  the length is %d"% (test3, detect.lengthOfLongestSubstring(test3)))
