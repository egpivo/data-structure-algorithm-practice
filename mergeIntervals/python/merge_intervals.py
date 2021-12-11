from collections import defaultdict
from typing import List


class SolutionSorting:
    """

    Complexity
    ----------
    - TC: O(n*long(n)) (sorting)
    - SC: O(n)
    """

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        new_intervals = []

        for interval in intervals:
            if new_intervals and new_intervals[-1][1] >= interval[0]:
                new_intervals[-1][1] = max(new_intervals[-1][1], interval[1])
            else:
                new_intervals.append(interval)
        return new_intervals


class SolutionGraph:
    """

    Complexity
    ----------
    - TC: O(n^2)
    - SC: O(n^2)
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        graph = self.build_graph(intervals)
        nodes_in_component, component_number = self.fetch_nodes_in_component(
            graph, intervals
        )
        return [
            self.merge_nodes(nodes_in_component[num]) for num in range(component_number)
        ]

    def is_overlapping(self, a, b):
        return a[1] >= b[0] and b[1] > a[0]

    def build_graph(self, intervals):
        graph = defaultdict(list)

        for i, interval in enumerate(intervals):
            for j in range(i + 1, len(intervals)):
                if self.is_overlapping(interval, intervals[j]):
                    graph[tuple(interval)].append(intervals[j])
                    graph[tuple(intervals[j])].append(interval)

        return graph

    def fetch_nodes_in_component(self, graph, intervals):
        visited = set()
        nodes_in_component = defaultdict(list)
        component_number = 0

        def mark_component_dfs(start):
            stack = [start]
            while stack:
                node = tuple(stack.pop())
                if node not in visited:
                    visited.add(node)
                    nodes_in_component[component_number].append(node)
                    stack.extend(graph[node])

        for interval in intervals:
            if tuple(interval) not in visited:
                mark_component_dfs(interval)
                component_number += 1

        return nodes_in_component, component_number

    def merge_nodes(self, nodes):
        min_start = min(node[0] for node in nodes)
        max_end = min(node[1] for node in nodes)
        return [min_start, max_end]


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(f"Solution is {SolutionSorting().merge(intervals)}")
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(f"Solution is {SolutionGraph().merge(intervals)}")
