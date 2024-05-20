class Solution:
    def isValidSudoku(self, board):

        def isRowValid(board):
            for row in board:
                if not isListValid(row):
                    return False
            return True

        def isColValid(board):
            # transpose the board via zip(*board)
            for col in zip(*board):
                if not isListValid(list(col)):
                    return False
            return True

        def isSubSquareValid(board):
            for i in [0, 3, 6]:
                for j in [0, 3, 6]:
                    ls = [board[x][y] for x in range(i, i + 3) for y in range(j, j+3)]
                    if not isListValid(ls):
                        return False
            return True

        def isListValid(ls):
            values = [i for i in ls if i != '.']
            return len(values) == len(set(values))

        return (isRowValid(board) and isSubSquareValid(board) and isColValid(board))
            
        
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3","",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(board))