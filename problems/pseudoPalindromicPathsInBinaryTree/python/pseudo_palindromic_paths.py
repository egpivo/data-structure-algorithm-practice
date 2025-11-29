from collections import defaultdict
from typing import Dict, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        result = 0

        def backtrack(path, node):
            nonlocal result
            if not node:
                return

            path[node.val] += 1

            if not node.left and not node.right:
                result += Solution.is_palindromic(path)

            if node.left:
                backtrack(path, node.left)
            if node.right:
                backtrack(path, node.right)

            path[node.val] -= 1

        backtrack(defaultdict(int), root)
        return result

    @staticmethod
    def is_palindromic(freq_dict: Dict[int, int]) -> bool:
        odd_count = sum(freq % 2 for freq in freq_dict.values())
        return odd_count <= 1
