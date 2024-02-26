from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    Complexity
    -----
    - TC: O(n)
    - SC: O(h)
    """

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
        elif not q or not p or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class Solution2:
    """
    Complexity
    -----
    - TC: O(n)
    - SC: O(h)
    """

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]

        while stack:
            current_p, current_q = stack.pop()

            if not current_p and not current_q:
                continue
            if not current_p or not current_q or current_p.val != current_q.val:
                return False

            stack.append((current_p.left, current_q.left))
            stack.append((current_p.right, current_q.right))

        return True


if __name__ == "__main__":
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)

    tree2 = TreeNode(3)
    tree2.left = TreeNode(9)
    tree2.right = TreeNode(20)
    tree2.right.left = TreeNode(15)
    tree2.right.right = TreeNode(7)

    print(Solution().isSameTree(tree, tree2))
    print(Solution2().isSameTree(tree, tree2))
