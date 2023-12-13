# Definition for a Node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SolutionRecursive:
    """

    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        answer = None

        def recurse_tree(node):
            nonlocal ans

            if not node:
                return False

            left = recurse_tree(node.left)
            right = recurse_tree(node.right)

            mid = node in (p, q)
            if mid + left + right >= 2:
                ans = node
            return mid or left or right

        recurse_tree(root)
        return answer


if __name__ == "__main__":
    p = TreeNode(5)
    p.left = TreeNode(6)
    p.right = TreeNode(2)
    p.right.left = TreeNode(7)
    p.right.right = TreeNode(4)

    q = TreeNode(1)
    q.left = TreeNode(0)
    q.right = TreeNode(8)
    node = TreeNode(3)
    node.left = p
    node.right = q

    print(f"{SolutionRecursive().lowestCommonAncestor(node, p, q).val}")
