from typing import Generator, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    """
    Notes
    ----
    - TC: O(1) (average)
    - SC: O(H)
    """

    def __init__(self, root: Optional[TreeNode]):
        self.iterator = self._inorder(root)
        self.next_value = next(self.iterator, None)

    def _inorder(self, node: Optional[TreeNode]) -> Generator[int, None, None]:
        if node:
            yield from self._inorder(node.left)
            yield node.val
            yield from self._inorder(node.right)

    def next(self) -> int:
        result = self.next_value
        self.next_value = next(self.iterator, None)
        return result

    def hasNext(self) -> bool:
        return self.next_value is not None
