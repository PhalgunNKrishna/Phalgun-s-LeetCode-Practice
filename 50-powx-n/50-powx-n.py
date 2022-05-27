class Solution:
    
    # My brute force solution basically --> basically the same as the given brute force solution
    def amyPow(self, x: float, n: int) -> float:
        
        ret = 1
        
        pos = abs(n)
        
        for i in range(pos):
            ret *= x
        
        if n < 0:
            ret = 1 / ret
            
        return ret
    
    # Brute Force Solution Taken from Given Solutions
    def bmyPow(self, x: float, n: int) -> float:
        
        if n < 0:
            x = 1 / x
            n = -n
        
        ret = 1
        
        for i in range(n):
            ret *= x
        
        return ret
    
    def fastPow(self, x: float, n: int) -> float:
        
        if n == 1:
            return x
        if n == 0:
            return 1.0
        
        halfPow = self.fastPow(x, n // 2)
        print('half = ', halfPow, n)
        
        if n % 2 == 0:
            return halfPow * halfPow
        else:
            return halfPow * halfPow * x
        
    def myPow(self, x: float, n: int) -> float:
        
        if n < 0:
            x = 1 / x
            n = -n
        
        return self.fastPow(x, n)
    
    