class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s
        
        rows = []
        
        for i in range(numRows):
            print(i)
            rows.append('')
        
        currRow = 0
        down = False
        
        for char in s:
            rows[currRow] += char
            if currRow == 0 or currRow == len(rows) - 1:
                down = not down
            if down:
                currRow += 1
            else:
                currRow -= 1
                    
        print(rows)
        ret = ''
        for i in rows:
            ret += (i)
            
        return ret