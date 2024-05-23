from typing import Optional, List
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                area = self.explore(grid, r, c)
                if max_area < area:
                    max_area = area
        return max_area

    # return size of island 
    # also sinks the landmass 
    def explore(self, grid, r, c) -> int:
        # Base Case: OOB 
        row_inbounds = 0 <= r < len(grid)
        col_inbounds = 0 <= c < len(grid[0])
        if not row_inbounds or not col_inbounds:
            return 0 

        # Base Case: not land
        if grid[r][c] != 1:
            return 0 

        grid[r][c] = '#'

        area = 1
        area += self.explore(grid, r-1, c)
        area += self.explore(grid, r+1, c)
        area += self.explore(grid, r, c-1)
        area += self.explore(grid, r, c+1)
        return area


grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
print(Solution().maxAreaOfIsland(grid))     # 6