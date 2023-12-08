class Solution:
    _char_mpa = {"{": "}", "(": ")", "[": "]"}

    def isValid(self, s: str) -> bool:
        if len(s) <= 1 or s[0] not in self._char_mpa or s[-1] in self._char_mpa:
            return False

        q = []
        remaining = ""
        matched_pattern = ""
        for char in s[:-1]:
            if char in self._char_mpa:
                q.append(self._char_mpa[char])
            else:
                matched_pattern += char
                if q:
                    remaining += q.pop()

        matched_pattern += s[-1]
        if q:
            remaining += "".join(q)
        return matched_pattern == remaining


class CleanerSolution:
    _char_mpa = {"{": "}", "(": ")", "[": "]"}

    def isValid(self, s: str) -> bool:
        if len(s) <= 1 or s[0] not in self._char_mpa or s[-1] in self._char_mpa:
            return False

        q = []
        for char in s:
            if char in self._char_mpa:
                q.append(self._char_mpa[char])
            else:
                if not q:
                    return False
                stacked_char = q.pop()
                if char != stacked_char:
                    return False

        return len(q) == 0


if __name__ == "__main__":
    s = "()[]{}"

    print(Solution().isValid(s))
    print(CleanerSolution().isValid(s))
