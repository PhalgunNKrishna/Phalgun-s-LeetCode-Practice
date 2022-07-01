class Solution:
    
    ### CLOSE BUT DID NOT SATISFY REQUIREMENT OF "EVERY PAIR OF ADJACENT INTEGERS DIFFERS BY EXACTLY ONE BIT"
    def agrayCode(self, n: int) -> List[int]:
        
        bitCombos = []
        
        def generateBits(currCombo):
            
            if len(currCombo) == n:
                bitCombos.append(currCombo)
                return
            
            currCombo += '0'
            generateBits(currCombo)
            currCombo = currCombo[:len(currCombo) - 1]
            currCombo += '1'
            generateBits(currCombo)
            
        generateBits("")
        
        print(bitCombos)
        
        ret = []
        
        for i in bitCombos:
            retVal = 0
            power = 0
            print('---')
            for j in range(len(i) - 1, -1, -1):
                print('j = ', i[j])
                retVal += int(i[j]) * int(math.pow(2, power))
                power += 1
            ret.append(retVal)
            
        return ret
    
    def grayCode(self, n: int) -> List[int]:
        if n == 0: return [0]
        arr = self.grayCode(n-1)
        return arr +  [(1<<(n-1)) + k for k in arr[::-1]]