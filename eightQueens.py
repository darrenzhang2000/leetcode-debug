import copy
class Solution:
    def solveNQueens(self, n):
        results = []
        board = [["."] * n for _ in range(n)]
        def backtrack(row, col):
            if row >= 0 and col >= 0:
                board[row][col] = "Q"
            if col == n - 1:
                print(board)
                results.append(copy.deepcopy(board))
            for i in range(n):
                if col < n - 1 and self.valid(i, col + 1, board, n):
                    backtrack(i, col + 1)
            board[row][col] = "."
        backtrack(-1, -1)
        return [["".join(arr) for arr in board] for board in results]
        # return results
        
    def valid(self, row, col, board, n):
        for i in range(n):
            if board[i][col] == "Q":
                return False
        for i in range(n):
            if board[row][i] == "Q":
                return False
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        i, j = row, col
        while i >= 0 and i < n and j >= 0:
            if board[i][j] == "Q":
                return False
            i += 1
            j -= 1        
        
        return True

s = Solution()
print(s.solveNQueens(5))