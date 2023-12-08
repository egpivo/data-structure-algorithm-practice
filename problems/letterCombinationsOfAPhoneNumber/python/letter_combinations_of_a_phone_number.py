from collections import deque
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(4^N * N)
    - SC: O(N)
    """

    _num_letter_map = {
        1: "",
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz",
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        q = deque(self._num_letter_map[int(digits[0])])

        for i in range(1, len(digits)):
            size = len(q)
            while size:
                char = q.popleft()
                for j in self._num_letter_map[int(digits[i])]:
                    q.append(char + j)

                size -= 1
        return q


class Solution2:
    """
    Complexity
    ----------
    - TC: O(4^N * N)
    - SC: O(N)
    """

    digit_map = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        ans = self.digit_map.get(digits[0])
        for digit in digits[1:]:
            ans = list(self.fetch_combination(ans, self.digit_map.get(digit)))
        return ans

    def fetch_combination(self, list_1, list_2):
        for l1 in list_1:
            for l2 in list_2:
                yield l1 + l2


class SolutionBacktracking:
    """
    Complexity
    ----------
    - TC: O(4^N * N)
    - SC: O(N)
    """

    digit_map = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        def backtrack(path, index):
            if len(path) == len(digits):
                combinations.append("".join(path))
                return

            for letter in self.digit_map.get(digits[index]):
                path.append(letter)
                backtrack(path, index + 1)
                path.pop()

        combinations = []
        backtrack([], 0)
        return combinations


if __name__ == "__main__":
    digits = "239"

    print(Solution().letterCombinations(digits))
    print(Solution2().letterCombinations(digits))
    print(SolutionBacktracking().letterCombinations(digits))
