from typing import List, Optional


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

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        reserved_answer = []
        if root is None:
            return reserved_answer

        stack_bag = [root]
        while stack_bag:
            bottom = stack_bag.pop()
            reserved_answer.append(bottom.val)

            if bottom.left:
                stack_bag.append(bottom.left)
            if bottom.right:
                stack_bag.append(bottom.right)
        return reserved_answer[::-1]


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)
    ans = Solution()
    print(f"The answer is {ans.postorderTraversal(tree)}")
