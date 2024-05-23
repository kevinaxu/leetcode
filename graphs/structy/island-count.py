from collections import deque
from pprint import pprint



def explore(grid, r, c, visited) -> bool:

    # Base Case: OOB 
    row_inbounds = 0 <= r < len(grid)
    col_inbounds = 0 <= c < len(grid[0])
    if not row_inbounds or not col_inbounds:
        return False 

    # Base Case: Water
    if grid[r][c] == 'W':
        return False 

    # Base Case: we've visited before
    pos = (r, c)
    if pos in visited:
        return False 

    # Main Logic: visit all nodes and mark as visited
    visited.add(pos)
    explore(grid, r-1, c, visited)
    explore(grid, r+1, c, visited)
    explore(grid, r, c-1, visited)
    explore(grid, r, c+1, visited)

    return True 




def island_count(grid):

    count, visited = 0, set() 
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid, r, c, visited):
                count += 1
    return count 


grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]
island_count(grid) # -> 3