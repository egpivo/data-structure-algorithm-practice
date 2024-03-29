# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: "Node") -> "Node":
        """
        Complexity
        ---------
        - p = # of nodes
        - TC: O(p)
        - SC: O(p)
        """
        if root is None:
            return None

        head, tail = None, None

        def inorder(node):
            nonlocal head, tail
            # base condition
            if node is None:
                return None

            inorder(node.left)
            if head is None:
                head = node
            else:
                tail.right = node
                node.left = tail
            tail = node
            inorder(node.right)

        inorder(root)
        if head and tail:
            head.left = tail
            tail.right = head

        return head
