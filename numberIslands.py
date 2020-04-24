class Solution:
    def numIslands(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        visited = [[False] * len(grid[0])] * len(grid)
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if self.isUnvisitedIsland(grid, visited, row, col):
                    if grid[row][col] == '1':
                        count += 1
                        self.visitIsland(grid, visited, row, col)
                    else:                     
                        visited[row][col] == True
        return count
    
    def isUnvisitedIsland(self, grid, visited, row, col):
        return visited[row][col] == False
    
    def visitIsland(self, grid, visited, row, col):
        print(row, col)
        if visited[row][col] == False:
            visited[row][col] = True
            if grid[row][col] == '1':
                if row - 1 >= 0:
                    self.visitIsland(grid, visited, row - 1, col)
                if col - 1 >= 0:
                    self.visitIsland(grid, visited, row, col - 1)
                if row + 1 < len(grid):
                    self.visitIsland(grid, visited, row + 1, col)
                if col + 1 < len(grid[0]):
                    self.visitIsland(grid, visited, row, col + 1)
        

s = Solution()
s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])