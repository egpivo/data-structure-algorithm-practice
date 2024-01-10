# Definition for a binary tree node.
from collections import defaultdict, deque
from typing import Dict, List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Complexity
    ----------
    - Time complexity: $O(N)$
    - Space complexity: $O(N)$
    """

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph: Dict[int, List[int]] = defaultdict(list)
        self.convert_graph(root, None, graph)
        return self.count_minutes(graph, start)

    def count_minutes(self, graph: Dict[int, List[int]], start: int) -> int:
        queue: deque = deque([(start, 0)])
        visited: set = set()

        while queue:
            node, depth = queue.popleft()
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, depth + 1))

        return depth

    def convert_graph(
        self,
        node: Optional[TreeNode],
        parent: Optional[TreeNode],
        graph: Dict[int, List[int]],
    ) -> None:
        if node:
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)

            self.convert_graph(node.left, node, graph)
            self.convert_graph(node.right, node, graph)
