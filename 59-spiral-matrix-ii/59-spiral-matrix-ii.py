class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        # Create all numbers to be used
        matrixLi = []
        for i in range(1, n * n + 1):
            matrixLi.append(i)
        
        matrix = []
        
        for i in range(n):
            matrix.append([])
        
        for i in range(len(matrix)):
            for j in range(n):
                matrix[i].append('a')
                        
        top = 1
        bottom = n - 1
        left = 0
        right = n - 1
        
        currDir = 'right'
        currX = 0
        currY = 0
        iteration = 0
        
        while iteration < len(matrixLi):
            
            if currDir == 'right':
                matrix[currY][currX] = matrixLi[iteration]
                print('right iter = ', matrix[currY][currX])
                if currX == right:
                    currDir = 'down'
                    right -= 1
                    currY += 1
                else:
                    currX += 1
            
            elif currDir == 'down':
                matrix[currY][currX] = matrixLi[iteration]
                print('down iter = ', matrix[currY][currX])
                if currY == bottom:
                    currDir = 'left'
                    bottom -= 1
                    currX -= 1
                else:
                    currY += 1
            
            elif currDir == 'left':                
                matrix[currY][currX] = matrixLi[iteration]
                print('left iter = ', matrix[currY][currX])
                if currX == left:
                    currDir = "up"
                    left += 1
                    currY -= 1
                else:
                    currX -= 1
            
            else:
                matrix[currY][currX] = matrixLi[iteration]
                print('up iter = ', matrix[currY][currX])
                if currY == top:
                    currDir = "right"
                    top += 1
                    currX += 1
                else:
                    currY -= 1
                
            iteration += 1
            
        return matrix