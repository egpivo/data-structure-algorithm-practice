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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        if root is None:
            return answer

        stack_bag = [root]
        while stack_bag:
            top = stack_bag.pop()
            answer.append(top.val)

            if top.right:
                stack_bag.append(top.right)
            if top.left:
                stack_bag.append(top.left)
        return answer


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)
    ans = Solution()
    print(f"The answer is {ans.preorderTraversal(tree)}")

