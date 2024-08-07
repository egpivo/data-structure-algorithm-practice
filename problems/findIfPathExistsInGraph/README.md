## [Find if Path Exists in Graph](https://leetcode.com/explore/learn/card/graph/619/depth-first-search-in-graph/3893/)
There is a **bi-directional** graph with n vertices, where each vertex is labeled from `0` to `n - 1` (**inclusive**). The edges in the graph are represented as a 2D integer array edges, where each edges`[i] = [ui, vi]` denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a **valid path** that exists from vertex start to vertex end.

Given `edges` and the integers `n`, `start`, and `end`, return true if there is a **valid path** from `start` to `end`, or `false` otherwise.

```
Input: n = 3, edges = [[0,1],[1,2],[2,0]], start = 0, end = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2
```

- My Solution: https://leetcode.com/problems/find-if-path-exists-in-graph/solutions/5052165/bfs-approach/
