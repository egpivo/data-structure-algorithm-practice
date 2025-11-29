from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        Find the shortest path in a binary matrix using BFS.
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        """
        n = len(grid)
        
        # Check if start or end cell is blocked
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1
        
        # 8-directional movements
        dirs = (
            (0, 1), (0, -1),
            (1, 0), (-1, 0),
            (1, 1), (-1, -1),
            (1, -1), (-1, 1)
        )
        
        q = deque([(0, 0, 1)])  # (row, col, path_length)
        seen = {(0, 0)}
        
        while q:
            r, c, step = q.popleft()
            
            # Check if we reached the destination
            if r == n - 1 and c == n - 1:
                return step
            
            # Explore all 8 directions
            for dr, dc in dirs:
                new_r, new_c = r + dr, c + dc
                
                # Check bounds, if cell is valid (0), and not visited
                if (0 <= new_r < n and 0 <= new_c < n and 
                    grid[new_r][new_c] == 0 and 
                    (new_r, new_c) not in seen):
                    seen.add((new_r, new_c))
                    q.append((new_r, new_c, step + 1))
        
        return -1


if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Simple 2x2 grid
    grid1 = [[0, 1], [1, 0]]
    result1 = solution.shortestPathBinaryMatrix(grid1)
    print(f"Test 1: {result1} (Expected: 2)")
    assert result1 == 2, "Test 1 failed"
    
    # Test case 2: 3x3 grid with clear path
    grid2 = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    result2 = solution.shortestPathBinaryMatrix(grid2)
    print(f"Test 2: {result2} (Expected: 4)")
    assert result2 == 4, "Test 2 failed"
    
    # Test case 3: Single cell (already at destination)
    grid3 = [[0]]
    result3 = solution.shortestPathBinaryMatrix(grid3)
    print(f"Test 3: {result3} (Expected: 1)")
    assert result3 == 1, "Test 3 failed"
    
    # Test case 4: Start cell blocked
    grid4 = [[1, 0], [0, 0]]
    result4 = solution.shortestPathBinaryMatrix(grid4)
    print(f"Test 4: {result4} (Expected: -1)")
    assert result4 == -1, "Test 4 failed"
    
    # Test case 5: End cell blocked
    grid5 = [[0, 0], [0, 1]]
    result5 = solution.shortestPathBinaryMatrix(grid5)
    print(f"Test 5: {result5} (Expected: -1)")
    assert result5 == -1, "Test 5 failed"
    
    # Test case 6: No path exists (middle column blocked)
    grid6 = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
    result6 = solution.shortestPathBinaryMatrix(grid6)
    print(f"Test 6: {result6} (Expected: -1)")
    assert result6 == -1, "Test 6 failed"
    
    # Test case 7: All zeros (straight diagonal path)
    grid7 = [[0, 0], [0, 0]]
    result7 = solution.shortestPathBinaryMatrix(grid7)
    print(f"Test 7: {result7} (Expected: 2)")
    assert result7 == 2, "Test 7 failed"
    
    print("\nAll test cases passed!")
