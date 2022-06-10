class Solution:
    
    minSum = -1
    
    ### CLOSE: EXCEEDED TIME LIMIT 
    def aminPathSum(self, grid: List[List[int]]) -> int:
        
        def findPath(currY, currX, currSum):
                        
            if currY == len(grid) - 1 and currX == len(grid[0]) - 1:
                self.minSum = currSum if self.minSum == -1 else min(self.minSum, currSum)
                return
            if currY < len(grid) - 1:
                findPath(currY + 1, currX, currSum + grid[currY + 1][currX])
            if currX < len(grid[0]) - 1:
                findPath(currY, currX + 1, currSum + grid[currY][currX + 1])
            if currY >= len(grid) - 1 or currX >= len(grid) - 1:
                return
            
        findPath(0, 0, grid[0][0])
            
        return self.minSum
    
    ### EXCEEDED TIME LIMIT AGAIN: TAKEN FROM SOLUTION
    def bminPathSum(self, grid: List[List[int]]) -> int:
        
        def findPath(currY, currX):
            if currY >= len(grid) or currX >= len(grid[0]):
                return math.inf
            if currY == len(grid) - 1 and currX == len(grid[0]) - 1:
                return grid[currY][currX]
            return grid[currY][currX] + min(findPath(currY + 1, currX), findPath(currY, currX + 1))
        
        return findPath(0, 0)
    
    ### DYNAMIC PROGRAMMING
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        dp =[['a'] * len(grid[0]) for i in range(len(grid))]
        print(dp)
        
        # LEARN REVERSED FOR LOOP
        # https://www.geeksforgeeks.org/backward-iteration-in-python/
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                if i == len(grid) - 1 and j != len(grid[0]) - 1:
                    print(i, j)
                    dp[i][j] = grid[i][j] + dp[i][j + 1]
                elif j == len(grid[0]) - 1 and i != len(grid) - 1:
                    dp[i][j] = grid[i][j] + dp[i + 1][j]
                elif i != len(grid) - 1 and j != len(grid[0]) - 1:
                    dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1])
                else:
                    dp[i][j] = grid[i][j]
        
        return dp[0][0]