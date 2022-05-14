class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def convertToInt(num):
            place = 1
            i = len(num) - 1
            ret = 0
            while (i >= 0):
                ret += int(num[i]) * place
                place = place * 10
                i -= 1
            return ret
        
        print(convertToInt(num2))
        
        return str(convertToInt(num1) * convertToInt(num2))