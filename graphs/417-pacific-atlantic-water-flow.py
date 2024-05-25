from typing import Optional, List
from collections import deque
from pprint import pprint

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def inbounds(r, c):
            r_inbounds = 0 <= r < len(heights)
            c_inbounds = 0 <= c < len(heights[0])
            return r_inbounds and c_inbounds


        def bfs(lst, visited):
            queue = deque(lst)
            while queue:
                r, c = queue.popleft()
                if (r, c) in visited:
                    continue
                visited.add((r, c))

                for dr, dc in directions:
                    nextR, nextC = dr + r, dc + c
                    if not inbounds(nextR, nextC):
                        continue
                    if heights[nextR][nextC] >= heights[r][c]:
                        queue.append((nextR, nextC))
            
            return visited 



        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        pacific, atlantic = [], [] 
        p_visited, a_visited = set(), set()

        for r in range(len(heights)):           # iterate over all rows 
            pacific.append((r, 0))
            atlantic.append((r, len(heights[0])-1))
        for c in range(len(heights[0])):        # iterate over columns 
            pacific.append((0, c))
            atlantic.append((len(heights)-1, c))

        bfs(pacific, p_visited)
        bfs(atlantic, a_visited)
        return list(p_visited.intersection(a_visited))




heights = [
    [1,2,2,3,5],
    [3,2,3,4,4],
    [2,4,5,3,1],
    [6,7,1,4,5],
    [5,1,1,2,4]
]
print(Solution().pacificAtlantic(heights))