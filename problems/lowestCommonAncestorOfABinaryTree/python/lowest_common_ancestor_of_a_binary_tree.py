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
    - TC: O(N)
    - SC: O(H)
    """

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if not root:
            return root

        lca = None

        def dfs(node):
            nonlocal lca

            if not node or lca:
                return False

            is_left = dfs(node.left)
            is_right = dfs(node.right)
            is_current = node in (p, q)

            if is_left + is_right + is_current >= 2:
                lca = node

            return is_left or is_right or is_current

        dfs(root)
        return lca


class SolutionParentPointer:
    """

    Complexity
    ----------
    - TC: O(N)
    - SC: O(H)
    """

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        parent = {root: None}
        ancestors = set()
        stack = [root]

        # Perform DFS to build parent pointers
        while p not in parent or q not in parent:
            node = stack.pop()

            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # Collect ancestors of node p
        while p:
            ancestors.add(p)
            p = parent[p]

        # Find the first common ancestor of p and q
        while q not in ancestors:
            q = parent[q]
        return q


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
    print(f"{SolutionParentPointer().lowestCommonAncestor(node, p, q).val}")
