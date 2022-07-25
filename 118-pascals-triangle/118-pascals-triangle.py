class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        currRow = 1
        ret = []
        
        while currRow < numRows + 1:
            
            level = []
            
            for i in range(currRow):
                level.append('a')
                
            level[0] = 1
            level[len(level) - 1] = 1
            
            if currRow > 2:
                for i in range(1, len(level) - 1):
                    print('i = ', i)
                    lastLevel = ret[len(ret) - 1]
                    print('last = ', lastLevel)
                    level[i] = lastLevel[i - 1] + lastLevel[i]
                        
            ret.append(level)
            
            print('ret = ', ret)
            
            currRow += 1
            
        return ret
            
            