from collections import deque


class SolutionBruteForce:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def is_duplicate(start: int, end: int) -> bool:
            chars = [0] * 128
            for i in range(start, end + 1):
                c = s[i]
                chars[ord(c)] += 1
                if chars[ord(c)] > 1:
                    return True
            return False

        n = len(s)
        res = 0
        for i in range(n):
            for j in range(i, n):
                if not is_duplicate(i, j):
                    res = max(res, j - i + 1)
        return res


class SolutionSlidingWindow:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0

        chars = [0] * 128
        max_len = len(s)
        ans = 0
        while right < max_len:
            r = s[right]
            chars[ord(r)] += 1

            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1

            ans = max(ans, right - left + 1)
            right += 1

        return ans


class Solution3:
    """
    Complexity
    ----------
    - Time complexity: O(n)
        - n: the length of s
    - Space complexity: O(min(m, n))
        - m is the size of the character set.
        - In the worst case, where all characters are unique, it would be O(n).

    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        max_length = 1
        char_index = {}

        for right, char in enumerate(s):
            if char in char_index:
                left = max(left, char_index[char] + 1)
            max_length = max(max_length, right - left + 1)
            char_index[char] = right

        return max_length


class Solution4:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = deque([])
        max_length = 0
        for char in s:
            max_length = max(max_length, len(queue))
            while char in queue:
                queue.popleft()
            queue.append(char)

        return max(max_length, len(queue))


if __name__ == "__main__":
    test1 = "abcabcbb"
    test2 = "bbbbb"
    test3 = "pwwkew"

    detect = Solution3()
    detect2 = SolutionBruteForce()
    detect3 = SolutionSlidingWindow()

    print(
        "Given %s  the length is %d" % (test1, detect.lengthOfLongestSubstring(test1))
    )
    print(
        "Given %s  the length is %d" % (test2, detect.lengthOfLongestSubstring(test2))
    )
    print(
        "Given %s  the length is %d" % (test3, detect.lengthOfLongestSubstring(test3))
    )

    print(
        "Given %s  the length is %d" % (test1, detect2.lengthOfLongestSubstring(test1))
    )
    print(
        "Given %s  the length is %d" % (test2, detect2.lengthOfLongestSubstring(test2))
    )
    print(
        "Given %s  the length is %d" % (test3, detect2.lengthOfLongestSubstring(test3))
    )

    print(
        "Given %s  the length is %d" % (test1, detect3.lengthOfLongestSubstring(test1))
    )
    print(
        "Given %s  the length is %d" % (test2, detect3.lengthOfLongestSubstring(test2))
    )
    print(
        "Given %s  the length is %d" % (test3, detect3.lengthOfLongestSubstring(test3))
    )
