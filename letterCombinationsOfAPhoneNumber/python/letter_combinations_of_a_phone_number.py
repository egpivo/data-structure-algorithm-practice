from collections import deque
from typing import List


class Solution:
    _num_letter_map = {
        1: "",
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz"
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


if __name__ == "__main__":
  digits = "23"

  print(Solution().letterCombinations(digits))
