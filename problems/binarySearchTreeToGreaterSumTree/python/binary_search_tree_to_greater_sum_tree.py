# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def reverse_inorder_traverse(node, accumulated_sum):
            if not node:
                return accumulated_sum
            accumulated_sum = reverse_inorder_traverse(node.right, accumulated_sum)

            node.val += accumulated_sum
            accumulated_sum = node.val
            return reverse_inorder_traverse(node.left, accumulated_sum)

        reverse_inorder_traverse(root, 0)
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
    root = [4,1,6,0,2,5,7, None,None,None,3,None,None,None,8]
    tree_root = list_to_treenode(root)

    converted_root = Solution().bstToGst(tree_root)
    print(inorder_traversal(converted_root))