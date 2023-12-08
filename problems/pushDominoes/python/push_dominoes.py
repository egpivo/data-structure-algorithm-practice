class Solution:
    """
    Two-pointers

    Complexity
    ----------
    - Time: O(n)
    - Space: O(n)
    """

    def pushDominoes(self, dominoes: str) -> str:
        ans = list(dominoes)

        left = 0
        for right, dominoe in enumerate(dominoes):
            if dominoe == ".":
                continue
            elif (dominoes[left] == dominoe) or (
                dominoes[left] == "." and dominoe == "L"
            ):
                ans[left : (right + 1)] = [dominoe] * (right - left + 1)
            elif dominoes[left] == "R" and dominoe == "L":
                mid = (right - left - 1) // 2
                for i in range(1, mid + 1):
                    ans[left + i] = "R"
                    ans[right - i] = "L"
            elif dominoes[left] == "L" and dominoe == "R":
                pass
            left = right

        if dominoes[left] == "R":
            ans[left:] = ["R"] * (len(dominoes) - left)

        return "".join(ans)


if __name__ == "__main__":
    dominoes = ".L.R...LR..L.."
    print(f"Solution: {Solution().pushDominoes(dominoes)}")
