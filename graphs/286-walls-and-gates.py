from typing import Optional, List
from collections import deque
from pprint import pprint


class Solution:

    # DFS, recursive - let's try this...
    # while this technically works, time complexity is not great: 
    # T: O(mn^2) 
    #   - the max depth of a dfs functions can be equal to the size of the grid (r * c)
    #   - worst case we might have to call this dfs function for all elements in grid O(rc ^ 2) 
    def explore(self, grid, r, c, visited, dist=0) -> None:

        # Base Case: OOB
        row_inbounds = 0 <= r < len(grid)
        col_inbounds = 0 <= c < len(grid[0])
        if not row_inbounds or not col_inbounds:
            return 

        # Base Case: Water
        if grid[r][c] == -1:
            return 

        # Base Case: Visited
        pos = (r, c)
        if pos in visited:
            return

        # Main Logic: 
        # If it's not water or 0, update the value to distance or min 
        visited.add(pos)
        if grid[r][c] > 0:
            if grid[r][c] == 2147483647:        # untouched ladn
                grid[r][c] = dist
            else:                               # nearest path 
                grid[r][c] = min(dist, grid[r][c])      

        dist += 1
        self.explore(grid, r-1, c, visited, dist)
        self.explore(grid, r+1, c, visited, dist)
        self.explore(grid, r, c-1, visited, dist)
        self.explore(grid, r, c+1, visited, dist)

    def wallsAndGates(self, grid: List[List[int]]) -> None:
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    self.explore(grid, r, c, set())


grid = [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]
Solution().wallsAndGates(grid)
pprint(grid)

# no chest in corner
# [
#     [4, -1, 0, 1], 
#     [3, 2, 1, -1], 
#     [4, -1, 2, -1], 
#     [-1, -1, 3, 4]
# ]

# [
#     [3, -1, 0, 1], 
#     [2, 2, 1, -1], 
#     [1, -1, 2, -1], 
#     [0, -1, 3, 4]
# ]

# output = [
#   [3,-1,0,1],
#   [2,2,1,-1],
#   [1,-1,2,-1],
#   [0,-1,3,4]
# ]