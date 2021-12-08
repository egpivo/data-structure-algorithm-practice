from collections import deque, defaultdict
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
                return (0, 0)

            left_child = helper(node.left)
            right_child = helper(node.right)

            rob = node.val + left_child[1] + right_child[1]
            non_rob = max(left_child) + max(right_child)
            return (rob, non_rob)

        return max(helper(root))


class SolutionDP:
    """

    Complexity
    ----------
    - TC: O(N)
    - SC: O(N)
    """

    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        tree = []
        graph = defaultdict(list)
        index = -1
        q = deque([(root, index)])

        while q:
            node, parent_index = q.popleft()
            if node:
                index += 1
                tree.append(node.val)
                graph[parent_index].append(index)
                q.append((node.left, index))
                q.append((node.right, index))

        dp_rob = [0] * (index + 1)
        dp_not_rob = [0] * (index + 1)

        for i in reversed(range(index + 1)):
            if not graph[i]:
                dp_rob[i] = tree[i]
            else:
                dp_rob[i] = tree[i] + sum(dp_not_rob[child_index] for child_index in graph[i])
                dp_not_rob[i] = sum(max(dp_rob[child_index], dp_not_rob[child_index]) for child_index in graph[i])
        return max(dp_rob[0], dp_not_rob[0])


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(1)

    print(f"Answer is {SolutionRecursive().rob(root)}")
    print(f"Answer is {SolutionDP().rob(root)}")