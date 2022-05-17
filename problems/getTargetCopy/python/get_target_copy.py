from collections import Counter


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        """
        Complexity
        ----------
        - TC: O(N)
        - SC: O(N)
        """
        answer = None

        def inorder(original, cloned):
            nonlocal answer
            if original:
                inorder(original.left, cloned.left)
                if original == target:
                    answer = cloned
                inorder(original.right, cloned.right)

        inorder(original, cloned)
        return answer
