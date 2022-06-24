class Solution:
    
    numWays = 0
        
    # WORKS BUT BS TIME LIMIT EXCEEDED
    def aclimbStairs(self, n: int) -> int:
        
        def calculateWays(currStep):
            
            if currStep == n:
                self.numWays += 1
                return
            
            if currStep > n:
                return
            
            else:
                calculateWays(currStep + 1)
                calculateWays(currStep + 2)
                
        calculateWays(0)
        
        return self.numWays
    
    # RECURSION DIFFERENT WAY 
    def bclimbStairs(self, n: int) -> int:
                
        def calculateWays(currStep):
            
            if currStep == n:
                return 1
            
            if currStep > n:
                return 0
            
            return calculateWays(currStep + 1) + calculateWays(currStep + 2)
        
        return calculateWays(0)
     
        
    # RECURSION WITH MEMOIZATION
    def climbStairs(self, n: int) -> int:
        
        ### STUDY THIS SYNTAX LATER
        memo = [0 for _ in range(n)]
        print(memo)
        
        def calculateWays(currStep, memo):
            
            if currStep == n:
                return 1
            
            if currStep > n:
                return 0
            
            if memo[currStep] > 0:
                return memo[currStep]
            
            memo[currStep] = calculateWays(currStep + 1, memo) + calculateWays(currStep + 2, memo)
            
            return memo[currStep]
        
        return calculateWays(0, memo)