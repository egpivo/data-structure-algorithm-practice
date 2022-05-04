class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """This is broute force version.
    
    Note
    ----
    - Time complexity: O(N)
    - Space complexity: O(N)
    """

    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.result = 0

        if root is None:
            return self.result

        self.calculate(root, root.val, root.val)
        return self.result

    def calculate(self, node: TreeNode, max_val: int, min_val: int) -> None:
        if node is None:
            return None

        self.result = max(self.result, abs(node.val - max_val), abs(node.val - min_val))

        max_val = max(node.val, max_val)
        min_val = min(node.val, min_val)

        self.calculate(node.left, max_val, min_val)
        self.calculate(node.right, max_val, min_val)


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.right = TreeNode(2)
    tree.right.right = TreeNode(0)
    tree.right.right.left = TreeNode(3)

    ans = Solution()
    print(f"The answer is {ans.maxAncestorDiff(tree)}")

