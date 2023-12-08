from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionBFS:
    """
    Notes
    -----
    - TC: O(n)
    - SC: O(n)
    """

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = [root]
        level = 1
        while queue:
            for _ in range(level):
                node = queue.pop(0)
                if not node:
                    continue
                if node.right:
                    queue.append(node.right)
                else:
                    queue.append(None)
                if node.left:
                    queue.append(node.left)
                else:
                    queue.append(None)

                node.left, node.right = node.right, node.left
            level = len(queue)
            for i in range(level // 2):
                if not (
                    (queue[i] is None and queue[level - i - 1] is None)
                    or (
                        queue[i]
                        and queue[level - i - 1]
                        and queue[level - i - 1].val == queue[i].val
                    )
                ):
                    return False

        return True


class SolutionDFS:
    """
    Notes
    -----
    - TC: O(n)
    - SC: O(n)
    """

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.is_mirror(root.left, root.right)

    def is_mirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return self.is_mirror(left.left, right.right) and self.is_mirror(
            left.right, right.left
        )
