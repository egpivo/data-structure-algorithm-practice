class Solution1:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def makeGood(self, s: str) -> str:
        stack = [s[0]]
        i = 1

        while i < len(s):
            while (
                i < len(s)
                and stack
                and (
                    (
                        stack[-1].isupper()
                        and s[i].islower()
                        and s[i] == stack[-1].lower()
                    )
                    or (
                        stack[-1].islower()
                        and s[i].isupper()
                        and s[i].lower() == stack[-1]
                    )
                )
            ):
                stack.pop()
                i += 1
            if i == len(s):
                break
            stack.append(s[i])
            i += 1

        return "".join(stack)


class Solution2:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def makeGood(self, s: str) -> str:
        stack = [s[0]] if s else []

        for i in range(1, len(s)):
            if stack and abs(ord(stack[-1]) - ord(s[i])) == 32:
                stack.pop()
            else:
                stack.append(s[i])

        return "".join(stack)


if __name__ == "__main__":
    s = "leEeetcode"

    print(Solution1().makeGood(s))
    print(Solution2().makeGood(s))
