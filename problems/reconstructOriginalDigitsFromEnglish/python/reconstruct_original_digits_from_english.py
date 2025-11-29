from collections import Counter


class Solution:
    """
    Idea
    ----
    - The most important thing we have to realize here is that some of the characters that make up the input string (S) can only belong to one possible word.
      This will immediately tell us how many of that digit should belong in our answer (ans).

    Note
    ----
    - s[i] \in ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"]
    """

    def originalDigits(self, s: str) -> str:
        freq = Counter(s)
        out = {}

        # zero
        out["0"] = freq["z"]
        # eight
        out["8"] = freq["g"]
        # two
        out["2"] = freq["w"]
        # four
        out["4"] = freq["u"]
        # six
        out["6"] = freq["x"]

        # three
        out["3"] = freq["h"] - out["8"]
        # five
        out["5"] = freq["f"] - out["4"]
        # seven
        out["7"] = freq["s"] - out["6"]
        # nine
        out["9"] = freq["i"] - out["5"] - out["6"] - out["8"]
        # one
        out["1"] = freq["n"] - out["7"] - 2 * out["9"]
        return "".join([key * out[key] for key in sorted(out.keys())])


class Solution2:
    """
    Idea
    ----
    - For python, using count() is actually faster than using a frequency map,
    """

    digits = [
        [0, "z", []],
        [2, "w", []],
        [4, "u", []],
        [6, "x", []],
        [8, "g", []],
        [1, "o", [0, 2, 4]],
        [3, "h", [8]],
        [5, "f", [4]],
        [7, "s", [6]],
        [9, "i", [6, 8, 5]],
    ]

    def originalDigits(self, s: str) -> str:
        freq_map, ans, n = [0] * 26, [0] * 10, len(s)

        for i in range(10):
            dig, char, rems = self.digits[i]
            count = s.count(char)
            for rem in rems:
                count -= ans[rem]
            ans[dig] += count
        return "".join([str(i) * ans[i] for i in range(10)])


if __name__ == "__main__":
    s = "owoztneoerowoztneoer"
    print(f"Solution: {Solution().originalDigits(s)}")
    print(f"Solution: {Solution2().originalDigits(s)}")
