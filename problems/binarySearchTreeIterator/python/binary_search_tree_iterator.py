from typing import Generator, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIteratorRecursive:
    """
    Notes
    ----
    - TC: O(1) (average)
    - SC: O(H)
    """

    def __init__(self, root: Optional[TreeNode]):
        self.inorder_generator = self._generate_inorder_value(root)
        self.next_value = next(self.inorder_generator, None)

    def _generate_inorder_value(
        self, node: Optional[TreeNode]
    ) -> Generator[int, None, None]:
        if node:
            yield from self._generate_inorder_value(node.left)
            yield node.val
            yield from self._generate_inorder_value(node.right)
        else:
            self.next_value = None

    def next(self) -> int:
        result, self.next_value = self.next_value, next(self.inorder_generator, None)
        return result

    def has_next(self) -> bool:
        return self.next_value is not None


class BSTIteratorStack:
    """
    Notes
    ----
    - TC: O(1) (average)
    - SC: O(H)
    """

    def __init__(self, root: Optional[TreeNode]) -> None:
        self.inorder_generator = self._generate_inorder_value(root)
        self.next_value = next(self.inorder_generator, None)

    def _generate_inorder_value(
        self, node: Optional[TreeNode]
    ) -> Generator[int, None, None]:
        stack = []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            yield node.val
            node = node.right

        self.next_value = None

    def next(self) -> Optional[int]:
        result, self.next_value = self.next_value, next(self.inorder_generator, None)
        return result

    def has_next(self) -> bool:
        return self.next_value is not None
