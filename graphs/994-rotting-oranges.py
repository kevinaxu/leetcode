from typing import Optional, List
from collections import deque
from pprint import pprint

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def inbounds(r, c):
            r_inbounds = 0 <= r < len(grid)
            c_inbounds = 0 <= c < len(grid[0])
            return r_inbounds and c_inbounds

        queue = deque()
        num_fresh_oranges = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    num_fresh_oranges += 1
                if grid[r][c] == 2:
                    queue.append((r, c))

        minute = 0
        
        # BFS 
        while queue and num_fresh_oranges > 0:
            minute += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    currR, currC = r + dr, c + dc

                    # Base Case: Ignore cell if OOB, Empty or Rotted
                    if not inbounds(currR, currC):
                        continue
                    if grid[currR][currC] == 0 or grid[currR][currC] == 2:
                        continue 

                    # Mark the orange as rotted
                    grid[currR][currC] = 2
                    num_fresh_oranges -= 1

                    queue.append((currR, currC))
        
        if num_fresh_oranges > 0:
            return -1 
        return minute
    


grid = [[2,1,1],[1,1,0],[0,1,1]]
print(Solution().orangesRotting(grid))
