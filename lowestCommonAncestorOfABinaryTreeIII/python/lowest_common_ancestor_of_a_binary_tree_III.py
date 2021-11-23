from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        Example
        -------
        1. p = 5; q = 1 --> return 3
        --> find the root; if p.parent is None: return root
        --> from p.value (a node can be a descendant of itself)

        5 --> 3
        1 --> 3

         Complexity
        ----------
        p: # of nodes
        TC: O(p)
        SC: O(1)
        """
        p1, q1 = p, q

        while p1 != q1:
            if p1.parent is None:
                p1 = q
            else:
                p1 = p1.parent
            if q1.parent is None:
                q1 = p1
            else:
                q1 = q1.parent
        return p1


class SolutionHashSet:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        Complexity
        ----------
        p: # of nodes
        TC: O(p)
        SC: O(p)
        """
        hash_set = set()

        while p:
            hash_set.add(p)
            p = p.parent
        while q:
            if q in hash_set:
                return q
            q = q.parent
        return None
