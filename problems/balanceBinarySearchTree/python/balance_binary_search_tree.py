# Definition for a binary tree node.
from collections import deque


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
    - SC: O(n)
    """
    def balanceBST(self, root: TreeNode) -> TreeNode:
        """ Balance the given BST. """
        sorted_values = self.inorder_traversal(root)
        return self.sorted_list_to_bst(sorted_values)

    def inorder_traversal(self, root: TreeNode) -> list:
        """ Perform an in-order traversal of the tree and return the node values in a sorted list. """
        values = []
        self._inorder_helper(root, values)
        return values

    def _inorder_helper(self, node: TreeNode, values: list):
        """ Helper function to recursively perform an in-order traversal. """
        if node:
            self._inorder_helper(node.left, values)
            values.append(node.val)
            self._inorder_helper(node.right, values)

    def sorted_list_to_bst(self, nums: list) -> TreeNode:
        """ Convert a sorted list to a balanced BST. """
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sorted_list_to_bst(nums[:mid])
        root.right = self.sorted_list_to_bst(nums[mid+1:])

        return root


def list_to_treenode(data):
    if not data:
        return None

    root = TreeNode(data[0])
    queue = deque([root])
    index = 1

    while queue:
        node = queue.popleft()

        if index < len(data) and data[index] is not None:
            node.left = TreeNode(data[index])
            queue.append(node.left)
        index += 1

        if index < len(data) and data[index] is not None:
            node.right = TreeNode(data[index])
            queue.append(node.right)
        index += 1

    return root

def inorder_traversal(root):
    result = []
    def traverse(node):
        if node:
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)
    traverse(root)
    return result


if __name__ == "__main__":
    root = [1, None,2,None,3, None,4, None, None]
    tree_root = list_to_treenode(root)

    converted_root = Solution().balanceBST(tree_root)
    print(inorder_traversal(converted_root))