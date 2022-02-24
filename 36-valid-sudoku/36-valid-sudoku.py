class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # ROWS
        for row in board:
            print('row = ', row)
            if self.validateRowCol(row) == False:
                return False
        
        print('-------')
        
        # COLUMNS
        for i in range(0, 9):
            col = []
            for j in range(0, 9):
                col.append(board[j][i])
            print('col = ', col)
            if self.validateRowCol(col) == False:
                return False
            
        rowT = 0
        colT = 0
        
        # SQUARES
        while rowT <= 8 and colT <= 8:
            square = []
            for i in range(rowT, rowT + 3):
                for j in range(colT, colT + 3):
                    square.append(board[i][j])
            if colT + 3 >= 8:
                rowT = rowT + 3
                colT = 0
            else:
                colT = colT + 3
            print(square)
            if self.validateRowCol(square) == False:
                return False
            
        
        return True
    
    def validateRowCol(self, batch: List[str]):
        numSet = set()
        
        for i in batch:
            if i in numSet and i.isnumeric():
                print('batch = ', batch)
                return False
            
            numSet.add(i)
        return True
        