class Solution:
    def reverse(self, x: int) -> int:
        
        s = str(x)
        retStr = ''
        neg = False
        
        if s[0] == '-':
            retStr += '-'
            j = len(s) - 1
            while j >= 1:
                retStr += s[j]
                j -= 1
        else:
            j = len(s) - 1
            while j >= 0:
                retStr += s[j]
                j -= 1
        
        if int(retStr) > 2**31 - 1 or int(retStr) < -2**31:
            return 0
        
        print(retStr)
            
        return int(retStr)
    