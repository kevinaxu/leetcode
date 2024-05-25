from typing import Optional, List
from collections import deque
from pprint import pprint

class Solution:
    '''
    Algorithm:
    - Iterate over the boundary of the board
        - If we encounter an "O" - we know that any region starting here can NOT be surrounded
        - DFS through and update all those "O" -> "#" (or other sentinel value) 
    - Now any "O" remaining are those that can be surrounded
        - any "#" can be switched back to "O"
    '''

    def solve(self, board: List[List[str]]) -> None:
        def inbounds(r, c):
            r_inbounds = 0 <= r < len(board)
            c_inbounds = 0 <= c < len(board[0])
            return r_inbounds and c_inbounds

        # recursive DFS
        def explore(r, c) -> None:
            if not inbounds(r, c):
                return 
            if board[r][c] in ['X', '#']:
                return 
            
            board[r][c] = '#'
            explore(r-1, c)
            explore(r+1, c)
            explore(r, c-1)
            explore(r, c+1)

        # first iteration: explore boundaries 
        for r in range(len(board)):
            for c in range(len(board[0])):
                if r == 0 or c == 0 or r == len(board)-1 or c == len(board[0])-1:
                    explore(r, c)

        # second pass: O -> X, # -> O 
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O': board[r][c] = 'X'
                if board[r][c] == '#': board[r][c] = 'O'



        
board = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]
]
Solution().solve(board)
print(board)