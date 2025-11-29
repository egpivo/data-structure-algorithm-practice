# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(h)
    """

    def averageOfSubtree(self, root: TreeNode) -> int:
        result = 0

        def dfs(node):
            nonlocal result
            if not node:
                return 0, 0

            left_subtree, left_count = dfs(node.left)
            right_subtree, right_count = dfs(node.right)
            val = node.val + left_subtree + right_subtree
            total_count = left_count + right_count + 1

            if node.val == val // total_count:
                result += 1

            return val, total_count

        _, _ = dfs(root)
        return result


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)
    tree.right.right = TreeNode(5)

    print(f"The DFS answer is {Solution().averageOfSubtree(tree)}")
