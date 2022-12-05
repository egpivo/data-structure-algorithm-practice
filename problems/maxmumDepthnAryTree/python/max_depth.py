
from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def dfs(node):
            if not node:
                return None
            
            answer.append(node.val)
            for child in node.children:
                dfs(child)
        
        answer = []
        dfs(root)
        return answer

    def postorder(self, root: 'Node') -> List[int]:
        def dfs(node):
            if not node:
                return None
            
            for child in node.children:
                dfs(child)
            answer.append(node.val)
        
        answer = []
        dfs(root)
        return answer

    def levelOrder(self, root: 'Node') -> List[List[int]]:
        queue = [root]
        answer = []

        if not root:
            return answer

        while queue:
            level = len(queue)
            level_vals = []
            for _ in range(level):
                node = queue.pop(0)
                
                if node.val is not None:
                    level_vals.append(node.val)
                for child in node.children:
                    queue.append(child)
            
            answer.append(level_vals)
            
        return answer
