from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join((key * value for key, value in Counter(s).most_common()))


if __name__ == "__main__":
    s = "tree"
    print(f"Solution: {Solution().frequencySort(s)}")
