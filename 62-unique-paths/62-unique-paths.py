class Solution:
    
    paths = 0
    
    
    ### CLOSE: TIME LIMIT EXCEEDED BS
    def auniquePaths(self, m: int, n: int) -> int:
                
        def calculatePath(currM, currN):
            if currM == m - 1 and currN == n - 1:
                self.paths += 1
                return
            elif currM > m or currN > n:
                return
            else:
                calculatePath(currM + 1, currN)
                calculatePath(currM, currN + 1)
                
        calculatePath(0, 0)
            
        return self.paths
    
    ### DYNAMIC PROGRAMMING
    def uniquePaths(self, m: int, n: int) -> int:
        
        # Study this syntax later:
        # d = [[1] * n for _ in range(m)]
        # SAME AS:
        # for i in range(m):
        #    d.append([])
        #    for j in range(n):
        #        d[i].append(1)
        
        d = [[1] * n for i in range(m)]
        print(d)
        
        for col in range(1, m):
            for row in range(1, n):
                d[col][row] = d[col - 1][row] + d[col][row - 1]
                
        return d[m - 1][n - 1]
        