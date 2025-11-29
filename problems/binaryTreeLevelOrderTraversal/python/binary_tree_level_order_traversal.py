from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Note
    ----
    - Time complexity: O(N)
    - Space complexity: O(N)
    """

    def levelOrderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        if root is None:
            return answer

        queue_bag = deque([root])
        while queue_bag:
            level = []
            level_size = len(queue_bag)
            for _ in range(level_size):
                node = queue_bag.pop(0)
                level.append(node.val)
                if node.left:
                    queue_bag.append(node.left)
                if node.right:
                    queue_bag.append(node.right)

            answer.append(level)
        return answer


if __name__ == "__main__":
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.left = TreeNode(7)
    ans = Solution()
    print(f"The answer is {ans.levelOrderTraversal(tree)}")
