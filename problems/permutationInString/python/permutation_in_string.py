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
        n1 = len(s1)
        n2 = len(s2)
        s1_freq = [0] * 26
        for char in s1:
            s1_freq[self.calculate_letter_index_from_a(char)] += 1

        s2_freq = [0] * 26
        for lo in range(n2 - n1 + 1):
            hi = lo + n1 - 1
            if lo == 0:
                for k in range(n1):
                    s2_freq[self.calculate_letter_index_from_a(s2[k])] += 1
            else:
                s2_freq[self.calculate_letter_index_from_a(s2[hi])] += 1

            if s1_freq == s2_freq:
                return True
            s2_freq[ord(s2[lo]) - ord('a')] -= 1

        return False

    @staticmethod
    def calculate_letter_index_from_a(lower_letter: str) -> int:
        return ord(lower_letter) - ord('a')


if __name__ == "__main__":
    s1 = "adc"
    s2 = "dcda"
    print(f"{Solution().checkInclusion(s1, s2)}")
