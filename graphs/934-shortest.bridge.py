from typing import Optional, List
from collections import deque
from pprint import pprint

class Solution:

    
    def shortestBridge(self, grid: List[List[int]]) -> int:
    
        visited = set() 
        direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def inbounds(r, c):
            row_inbounds = 0 <= r < len(grid)
            col_inbounds = 0 <= c < len(grid)
            return row_inbounds and col_inbounds

        # DFS / Recursive 
        # Modify island so that it can be distinguished from other 
        def dfs(r, c) -> None:

            if not inbounds(r, c):  return 
            if grid[r][c] != 1:     return 
            if (r, c) in visited:   return 

            
            visited.add((r, c))

            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        # BFS / iterative
        def bfs():
            result, queue = 0, deque(visited)
            while queue: 
                for _ in range(len(queue)):     # iterate level by level 
                    r, c = queue.popleft()

                    for dr, dc in direct:
                        currR, currC = r + dr, c + dc
                        if not inbounds(currR, currC) or (currR, currC) in visited:
                            continue
                        if grid[currR][currC]:
                            return result
                        queue.append((currR, currC))
                        visited.add((currR, currC))
                result += 1        

        
        # Find first island and modify it (1 --> 2)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:     # found first island
                    dfs(r, c)           # modify first island to 2 
                    return bfs()

grid = [[0,1,0],[0,0,0],[0,0,1]]
# grid = [
#     [1,1,1,1,1],
#     [1,0,0,0,1],
#     [1,0,1,0,1],
#     [1,0,0,0,1],
#     [1,1,1,1,1]
# ]
print(Solution().shortestBridge(grid))
