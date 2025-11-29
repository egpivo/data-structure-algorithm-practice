from collections import defaultdict
from typing import List


class Solution1:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(int)
        max_node = None

        for src, des in edges:
            graph[src] += 1
            graph[des] += 1

            if max_node is None or graph[src] > graph[max_node]:
                max_node = src
            if graph[des] > graph[max_node]:
                max_node = des

        return max_node


class Solution2:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        sign = "-" if num < 0 else ""
        remainders = []
        abs_num = abs(num)
        while abs_num:
            remainders.append(str(abs_num % 7))
            abs_num //= 7
        remainders.append(sign)
        return "".join(reversed(remainders))


class Solution2:
    """
    Complexity
    ----------
    - TC: O(1)
    - SC: O(1)
    """

    def findCenter(self, edges: List[List[int]]) -> int:
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]


if __name__ == "__main__":
    edges = [[1, 2], [2, 3], [4, 2]]
    print(f"The solution is {Solution1().findCenter(edges)}")
    print(f"The solution is {Solution2().findCenter(edges)}")
