from typing import Optional


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
    - Space complexity: O(H)
    """

    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None

            # Traverse left and right subtrees
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            # Check if current node is a leaf node with target value
            if node.left is None and node.right is None and node.val == target:
                return None

            return node

        return dfs(root)


def display_tree(root):
    def traverse(node):
        if node:
            print(node.val, end=" ")
            traverse(node.left)
            traverse(node.right)
        else:
            print("None", end=" ")

    traverse(root)


if __name__ == "__main__":
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.left = TreeNode(7)
    ans = Solution().removeLeafNodes(tree, 7)
    print("Modified Tree:")
    display_tree(ans)
