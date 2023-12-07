
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    """
    Notes
    -----
    - TC: O(n^2)
    - SC: O(n)
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:index + 1], inorder[:index + 1])
        root.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        return root

class Solution2:
    """
    Notes
    -----
    - TC: O(n)
    - SC: O(n)
    """

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        inorder_map = {key: index for index, key in enumerate(inorder)}

        def helper(left, right):
            if left > right:
                return None
            root = TreeNode(postorder.pop())
            index = inorder_map[root.val]
            root.right = helper(index + 1, right)
            root.left = helper(left, index - 1)
            return root
        return helper(0, len(inorder) - 1)
