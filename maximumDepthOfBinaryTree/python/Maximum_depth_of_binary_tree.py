# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == "__main__":
  tree = TreeNode(3)
  tree.left = TreeNode(9)
  tree.right = TreeNode(20)
  tree.right.left = TreeNode(15)
  tree.right.right = TreeNode(7)

  ans = Solution()
  print(ans.maxDepth(tree))
