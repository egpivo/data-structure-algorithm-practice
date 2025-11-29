from collections import deque


# Definition for a binary tree node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    """
    Notes
    -----
    - TC: O(n)
    - SC: O(n)
    """

    def connect(self, root: "Node") -> "Node":
        if not root:
            return root
        queue = deque([root])

        while queue:
            level = len(queue)
            for index in range(level):
                node = queue.popleft()

                if index < level - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root


class Solution2:
    """
    Notes
    -----
    - TC: O(n)
    - SC: O(1)
    """

    def connect(self, root: "Node") -> "Node":
        if not root:
            return root

        current_level_start = root
        next_level_dummy = Node()

        while current_level_start:
            current = current_level_start
            previous = next_level_dummy
            while current:
                if current.left:
                    previous.next = current.left
                    previous = previous.next
                if current.right:
                    previous.next = current.right
                    previous = previous.next
                current = current.next
            current_level_start = next_level_dummy.next
            next_level_dummy.next = None
        return root
