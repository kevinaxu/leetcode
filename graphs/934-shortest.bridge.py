from typing import Optional, List
from collections import deque
from pprint import pprint

class Solution:

    # DFS / Recursive 
    # Modify island so that it can be distinguished from other 
    def dfs(self, grid, r, c) -> None:
        # Base Case: OOB 
        row_inbounds = 0 <= r < len(grid)
        col_inbounds = 0 <= c < len(grid)
        if not row_inbounds or not col_inbounds:
            return 

        if grid[r][c] != 1:
            return 

        grid[r][c] = 2
        self.dfs(grid, r-1, c)
        self.dfs(grid, r+1, c)
        self.dfs(grid, r, c-1)
        self.dfs(grid, r, c+1)
        

    # BFS / Iterative  
    # (r, c) is the index of the second island 
    def bfs(self, grid, r, c):

        visited = set()

        queue = deque([ (r, c, 0) ])
        while queue:
            r, c, dist = queue.popleft()

            # Base Case: OOB
            row_inbounds = 0 <= r < len(grid)
            col_inbounds = 0 <= c < len(grid)
            if not row_inbounds or not col_inbounds:
                continue        # just skip this tuple

            # Base Case: Already visited
            if (r, c) in visited:
                continue
            visited.add((r, c))

            print("processing", r, c)

            # Base Case: Found other island 
            # dist - 1 since we only care about the water nodes
            if grid[r][c] == 1 and dist > 0:
                return dist - 1         

            # Main Logic:  
            queue.append((r-1, c, dist + 1))
            queue.append((r+1, c, dist + 1))
            queue.append((r, c-1, dist + 1))
            queue.append((r, c+1, dist + 1))

        return 



    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:             # found first island
                    self.dfs(grid, r, c)        # modify first island to 2 
                    self.bfs(grid, r, c)
                    return 

grid = [[0,1,0],[0,0,0],[0,0,1]]
# grid = [
#     [1,1,1,1,1],
#     [1,0,0,0,1],
#     [1,0,1,0,1],
#     [1,0,0,0,1],
#     [1,1,1,1,1]
# ]
Solution().shortestBridge(grid)
pprint(grid)