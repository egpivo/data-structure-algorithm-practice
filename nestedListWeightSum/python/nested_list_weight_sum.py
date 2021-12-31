from typing import List


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#


class SolutionDFS:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def depthSum(self, nestedList: List[NestedInteger]) -> int:

        def dfs(nested_list, depth):
            total = 0
            for nested_obj in nested_list:
                if nested_obj.isInteger():
                    total += nested_list.getInteger() * depth
                else:
                    total += dfs(nested_obj.getList(), depth + 1)

            return total

        return dfs(nestedList, 1)


class SolutionBFS:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        q = deque(nestedList)
        depth = 0
        total = 0
        while q:
            depth += 1
            level = len(q)
            for _ in range(level):
                nested_obj = q.popleft()
                if nested_obj.isInteger():
                    total += nested_obj.getInteger() * depth
                else:
                    q.extend(nested_obj.getList())
        return total
