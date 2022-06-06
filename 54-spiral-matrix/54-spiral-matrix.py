class Solution:
    
    # Approach 1: Initialize Boundaries
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = []
        
        numRows = len(matrix)
        numCols = len(matrix[0])
        
        top = 1
        left = 0
        bottom = numRows - 1
        right = numCols - 1
        
        iterations = 0
        
        currDirection = "right"
        currX = 0
        currY = 0
        
        res.append(matrix[currY][currX])
        
        while len(res) < numRows * numCols:
            
            if currDirection == "right":
                if currX == right:
                    right = currX - 1
                    currDirection = "down"
                    continue
                else:
                    currX += 1
            
            elif currDirection == "down":
                if currY == bottom:
                    bottom = bottom - 1
                    currDirection = "left"
                    continue
                else:
                    currY += 1
            
            elif currDirection == "left":
                if currX == left:
                    left = currX + 1
                    currDirection = "up"
                    continue
                else:
                    currX -= 1
            
            elif currDirection == "up":
                if currY == top:
                    top = currY + 1
                    currDirection = "right"
                    continue
                else:
                    currY -= 1
            
            print([currY, currX])
                
            res.append(matrix[currY][currX])
            
        return res