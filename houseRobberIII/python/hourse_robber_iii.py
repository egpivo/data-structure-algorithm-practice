from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionRecursive:
    """

    Complexity
    ----------
    - TC: O(N)
    - SC: O(N)
    """
    def rob(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return (0 , 0)

            left_child = helper(node.left)
            right_child = helper(node.right)

            rob = node.val + left_child[1] + right_child[1]
            non_rob = max(left_child) + max(right_child)
            return (rob, non_rob)

        return max(helper(root))



if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(1)

    print(f"Answer is {SolutionRecursive().rob(root)}")
