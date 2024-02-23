from collections import defaultdict, deque
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(E + k)
    - SC: O(V)
    """

    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        graph = defaultdict(list)

        # Build the graph using defaultdict
        for start, end, price in flights:
            graph[start].append((end, price))

        # Initialize variables
        queue = deque([(src, 0, 0)])  # Added the third element for tracking steps
        visited = defaultdict(lambda: float("inf"))  # Initialize with infinity

        # Breadth-first search
        while queue:
            current_city, current_cost, steps = queue.popleft()

            if steps <= k:
                for next_city, next_cost in graph.get(current_city, []):
                    total_cost = current_cost + next_cost
                    if total_cost < visited[next_city]:
                        visited[next_city] = total_cost
                        queue.append((next_city, total_cost, steps + 1))

        return visited[dst] if dst in visited else -1


if __name__ == "__main__":
    n = 4
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    src = 0
    dst = 3
    k = 1
    print(f"The solution is {Solution().findCheapestPrice(n, flights, src, dst, k)}")
