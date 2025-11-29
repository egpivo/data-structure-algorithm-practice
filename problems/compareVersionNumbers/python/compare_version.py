from collections import deque


class Solution:
    """
    Complexity
    ----------
    - TC: O(n+m)
    - SC: O(n+m)
    """

    def compareVersion(self, version1: str, version2: str) -> int:

        queue1 = self.parse_version(version1)
        queue2 = self.parse_version(version2)

        while queue1 and queue2:
            num1 = queue1.popleft()
            num2 = queue2.popleft()
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1

        while queue1:
            if queue1.popleft() > 0:
                return 1
        while queue2:
            if queue2.popleft() > 0:
                return -1

        return 0

    @staticmethod
    def parse_version(version: str) -> deque:
        return deque(map(int, version.split(".")))


if __name__ == "__main__":
    version1 = "0.1"
    version2 = "1.1"
    print(f"The solution is {Solution().compareVersion(version1, version2)}")
