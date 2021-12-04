class Solution:
    """
    Note
    ----
    - sliding window

    Complexity
    ----------
    - SC: O(len(s1) + 26* (len(s1) - len(s2)))
    - TC: O(1)
    """

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = [0] * 26
        for char in s1:
            s1_freq[ord(char) - ord('a')] += 1

        s2_freq = [0] * 26
        for lo in range(len(s2) - len(s1) + 1):
            hi = lo + len(s1) - 1
            if lo == 0:
                for k in range(len(s1)):
                    s2_freq[ord(s2[k]) - ord('a')] += 1
            else:
                s2_freq[ord(s2[hi]) - ord('a')] += 1

            if s1_freq == s2_freq:
                return True
            s2_freq[ord(s2[lo]) - ord('a')] -= 1

        return False


if __name__ == "__main__":
    s1 = "adc"
    s2 = "dcda"
    print(f"{Solution().checkInclusion(s1, s2)}")
