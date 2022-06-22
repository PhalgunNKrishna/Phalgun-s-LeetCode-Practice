class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        strA = list(a)
        strB = list(b)
        
        sumList = []
        
        aIter = len(strA) - 1
        bIter = len(strB) - 1
        rem = 0
        
        while aIter >= 0 or bIter >= 0:
            
            currSum = 0
            
            if aIter >= 0 and bIter >= 0:
                currSum = int(strA[aIter]) + int(strB[bIter]) + rem
            
            elif aIter >= 0 and bIter < 0:
                currSum = int(strA[aIter]) + rem
            
            else:
                currSum = int(strB[bIter]) + rem
            
            sumList.insert(0, currSum % 2)
            rem = currSum // 2
            
            aIter -= 1
            bIter -= 1
        
        if rem:
            sumList.insert(0, rem)
            
        ret = ""
        
        for i in sumList:
            ret += str(i)
        
        return ret