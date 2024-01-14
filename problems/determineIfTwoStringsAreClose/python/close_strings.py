from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        freq1, freq2 = Counter(word1), Counter(word2)
        return freq1.keys() == freq2.keys() and sorted(freq1.values()) == sorted(
            freq2.values()
        )


if __name__ == "__main__":
    print(f"Solution: {Solution().closeStrings( 'abc', 'bca')}")
