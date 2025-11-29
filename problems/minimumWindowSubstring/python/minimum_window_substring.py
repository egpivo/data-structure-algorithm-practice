from collections import Counter


class Solution:
    """
    Complexity
    ----------
    - TC: O(m+n)
    - SC: O(m+n)
    """

    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)

        freq_t = Counter(t)
        freq_s = Counter()

        required_chars = len(freq_t)
        formed_chars = 0
        min_length = float("inf")
        result = ""

        left = right = 0

        while right < m:
            char = s[right]
            freq_s[char] += 1

            if char in freq_t and freq_s[char] == freq_t[char]:
                formed_chars += 1

            while formed_chars == required_chars:
                current_length = right - left + 1
                if current_length < min_length:
                    min_length = current_length
                    result = s[left : right + 1]

                char_left = s[left]
                freq_s[char_left] -= 1

                if char_left in freq_t and freq_s[char_left] < freq_t[char_left]:
                    formed_chars -= 1
                left += 1
            right += 1

        return result


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print(f"Solution: {Solution().minWindow(s, t)}")
