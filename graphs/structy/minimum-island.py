

def explore(grid, r, c, visited) -> int:

    # Base Case: OOB 
    row_inbounds = 0 <= r < len(grid)
    col_inbounds = 0 <= c < len(grid[0])
    if not row_inbounds or not col_inbounds:
        return 0

    # Base Case: Water
    if grid[r][c] == 'W':
        return 0

    # Base Case: we've visited before
    pos = (r, c)
    if pos in visited:
        return 0 

    # Main Logic: visit all nodes and mark as visited
    visited.add(pos)

    left = explore(grid, r-1, c, visited)
    right = explore(grid, r+1, c, visited)
    up = explore(grid, r, c-1, visited)
    down = explore(grid, r, c+1, visited)

    return 1 + left + right + up + down


def minimum_island(grid):
    visited = set() 
    min_size = len(grid) * len(grid[0])
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = explore(grid, r, c, visited)
            if size > 0 and size < min_size:
                min_size = size
    return min_size 


grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]
print(minimum_island(grid)) # -> 2