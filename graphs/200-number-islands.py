from typing import Optional, List
from collections import deque


class Solution:

    # DFS / Recursive 
    # Alternate solution where we modify the input Grid in-place
    # T: Same as before -> iteration O(r*c) + DFS O(r*c) -> O(rc) 
    # S: O(1) - modifies in place instead of maintaining visited set() 
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):

                # if we encounter land, sink the land mass and increment 
                if grid[r][c] == '1':
                    self.explore(grid, r, c)
                    count += 1
        return count

    def explore(self, grid, r, c) -> bool:

        # Base Case: bounds
        row_inbounds = 0 <= r < len(grid)
        col_inbounds = 0 <= c < len(grid[0])
        if not row_inbounds or not col_inbounds:
            return False 

        # Base Case: water
        if grid[r][c] != '1':
            return False 

        grid[r][c] = "#"
        self.explore(grid, r-1, c)
        self.explore(grid, r+1, c)
        self.explore(grid, r, c-1)
        self.explore(grid, r, c+1)

        return True 


    # DFS / Recursive 
    # Iterative function to go through all elemetns in the grid
    # explore() -> method that returns True if we've reached an unexplored island
    #
    # T: We're iterating over the entire grid. Worst case entire island is Land
    #   Iteration O(r*c) + DFS O(r*c) --> O(rc) 
    # S: storing visited - entrries for every position O(rc) 
    #    
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     count, visited = 0, set()
    #     for r in range(len(grid)):
    #         for c in range(len(grid[0])):
    #             if self.explore(grid, r, c, visited):
    #                 count += 1
    #     return count

    # def explore(self, grid, r, c, visited) -> bool:
    #     # Base Case: bounds
    #     row_inbounds = 0 <= r < len(grid)
    #     col_inbounds = 0 <= c < len(grid[0])
    #     if not row_inbounds or not col_inbounds:
    #         return False 

    #     # Base Case: water
    #     if grid[r][c] == '0':
    #         return False 

    #     # Base Case: visited
    #     pos = (r, c)
    #     if pos in visited:
    #         return False 

    #     visited.add(pos)
    #     self.explore(grid, r-1, c, visited)
    #     self.explore(grid, r+1, c, visited)
    #     self.explore(grid, r, c-1, visited)
    #     self.explore(grid, r, c+1, visited)

    #     return True 


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(Solution().numIslands(grid))      # 1
