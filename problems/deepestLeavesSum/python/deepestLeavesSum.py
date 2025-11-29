from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return None

        queue_bag = [root]
        while queue_bag:
            level_size = len(queue_bag)
            answer = 0

            for _ in range(level_size):
                node = queue_bag.pop(0)
                answer += node.val

                if node.left is not None:
                    queue_bag.append(node.left)
                if node.right is not None:
                    queue_bag.append(node.right)

        return answer


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.right = TreeNode(6)
    tree.left.left.left = TreeNode(7)
    tree.right.right.right = TreeNode(8)
    ans = Solution()
    print(f"The answer is {ans.deepestLeavesSum(tree)}")
