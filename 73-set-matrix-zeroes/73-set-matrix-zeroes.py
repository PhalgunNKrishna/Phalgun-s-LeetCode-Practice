class Solution:
    
    ## CLOSE, element that was previously 0 before alteration may still show up in altered list if something in row / col was a 0 as well
    def asetZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        altered = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0 and (i, j) not in altered:
                    for a in range(len(matrix[i])):
                        matrix[i][a] = 0
                        altered.append((i, a))
                    for a in range(len(matrix)):
                        matrix[a][j] = 0
                        altered.append((a, j))
        
        print(altered)
        return matrix
    
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        zeroLocations = []
        
        # FIRST PASS: FIND WHERE THE ZEROES ARE
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zeroLocations.append((i, j))
                    
        print(zeroLocations)
        
        # SECOND PASS: alter matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (i, j) in zeroLocations:
                    for a in range(len(matrix[i])):
                        matrix[i][a] = 0
                    for a in range(len(matrix)):
                        matrix[a][j] = 0
        
        return matrix