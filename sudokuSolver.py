class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        
        # def backtrack(row, col):
        #     print(row, col)
        #     if col == 9: #out of bounds
        #         if row == 8: #sudoku solved
        #             return board
        #         else:
        #             backtrack(row + 1, 0) #procede to next row
        #     if board[row][col] == ".":
        #         for i in range(1, 10):
        #             if self.valid(row, col, str(i), board):
        #                 board[row][col] = str(i)
        #                 backtrack(row, col + 1)
        #         board[row][col] = "."
        #     else:
        #         backtrack(row, col + 1)
        # backtrack(0, 0)
        def backtrack(row, col):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == ".":
                        for i in range(1, 10):
                            if self.valid(i, j, str(i), board):
                                board[i][j] = str(i)

    def valid(self, row, col, i, board):
        for j in range(9):
            # print(board[row][col] == i, row, col, j)

            if board[row][j] == i:
            
                return False
            if board[j][col] == i:
                return False
        #find which row and col the grid starts
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for r in range(row_start, row_start + 3):
            for c in range(col_start, col_start + 3):
                if board[r][c] == i:
                    return False
        return True
                    
            
s = Solution()
s.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])

# arr = [[1, 2, '.',1, 2, '.', 1, 2, '.'],['.', '.', '.', 1, 2, '.', 1, 2, '.'],['.', '.', '.',1, 2, '.',1, 2, '.'] ,[1, 2, '.',1, 2, '.', 1, 2, '.'],['.', '.', '.', 1, 2, '.', 1, 2, '.'],['.', '.', '.',1, 2, '.',1, 2, '.'] ,[1, 2, '.',1, 2, '.', 1, 2, '.'],['.', '.', '.', 1, 2, '.', 1, 2, '.'],['.', '.', '.',1, 2, '.',1, 2, '.'] ]

# print(s.valid(0, 2, 9, arr))

