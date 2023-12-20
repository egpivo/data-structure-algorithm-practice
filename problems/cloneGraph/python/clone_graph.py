from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class SolutionDFS:
    def cloneGraph(self, node: "Node") -> "Node":
        """
        Complexity
        ----------
        - N: # of nodes
        - M: # of edges
        - TC: O(N+M)
        - SC: O(N)
            - visited hash map
        """
        visited = {}

        def dfs(node):
            if node is None:
                return
            if node in visited:
                return visited[node]
            else:
                cloned_node = Node(node.val)
                visited[node] = cloned_node
            if node.neighbors:
                for i in node.neighbors:
                    cloned_node.neighbors.append(dfs(i))
            return cloned_node

        return dfs(node)


class SolutionBFS:
    """
    Notes
    -----
    - V: the number of nodes in the graph
    - TC: O(V)
    - SC: O(V)
    """

    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return None

        visited = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            current_node = queue.popleft()
            for neighbor in current_node.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                visited[current_node].neighbors.append(visited[neighbor])

        return visited[node]
