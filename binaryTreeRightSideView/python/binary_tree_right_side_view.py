from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class DFSSolution:
    """
    Note
    ----
    - Time complexity: O(N)
    - Space complexity: O(H)
    """
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        answer = []
        def search_by_level(node: TreeNode, level: int) -> None:
            if level == len(answer):
                answer.append(node.val)

            for child in (node.right, node.left):
                if child:
                    search_by_level(child, level + 1)

        search_by_level(root, 0)
        return answer

class BFSSolution:
    """
    Note
    ----
    - Time complexity: O(N)
    - Space complexity: O(D)
    """    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        if root is None:
            return answer  
        q = deque([root])

        answer = []
        while q:
            level_length = len(q)
            
            for i in range(level_length):
                node = q.popleft()
                if i == level_length - 1:
                    answer.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return answer




if __name__ == "__main__":
    tree = TreeNode(1)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)
    tree.right.right = TreeNode(5)

    print(f"The DFS answer is {DFSSolution().rightSideView(tree)}")
    print(f"The BFS answer is {BFSSolution().rightSideView(tree)}")
        

