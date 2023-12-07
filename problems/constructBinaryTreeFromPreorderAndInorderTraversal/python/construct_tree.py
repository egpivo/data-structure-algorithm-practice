
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

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        value = postorder[-1]
        index = inorder.index(value)
        root = TreeNode(value)
        root.left = self.buildTree(inorder[:index+1], postorder[:index])
        root.right = self.buildTree(inorder[index+1:], postorder[index:-1])

        return root

class Solution2:
    """
    Notes
    -----
    - TC: O(n^2)
    - SC: O(n)
    """

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        value = postorder.pop()
        index = inorder.index(value)
        root = TreeNode(value)
        root.left = self.buildTree(inorder[:index+1], postorder[:index])
        root.right = self.buildTree(inorder[index+1:], postorder[index:])

        return root

class Solution3:
    """
    Notes
    -----
    - TC: O(n)
    - SC: O(n)
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: index for index, val in enumerate(inorder)}

        def helper(left, right):
            if left > right:
                return None
            root = TreeNode(preorder.pop(0))
            index = inorder_map[root.val]
            root.left = helper(left, index - 1)
            root.right = helper(index + 1, right)
            return root

        return helper(0, len(inorder) - 1)

