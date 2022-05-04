from typing import Optional, List

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
    - Space complexity: O(N)
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack_bag = []
        answer = []

        if root is None:
            return stack_bag

        while root or stack_bag:
            while root:
                stack_bag.append(root)
                root = root.left

            root = stack_bag.pop()
            answer.append(root.val)
            root = root.right

        return answer

class SolutionRecursive:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

if __name__ == "__main__":
    tree = TreeNode(1)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)
    ans = Solution()
    print(f"The answer is {ans.inorderTraversal(tree)}")
    print(f"The recurisve answer is {SolutionRecursive().inorderTraversal(tree)}")

