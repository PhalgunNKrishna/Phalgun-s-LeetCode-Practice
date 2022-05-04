class Solution:
    
    def generate(self, n, digitString):
        if n == 1:
            return digitString + '1'
        else:
            ret = ""
            start = 0
            for i in range(len(digitString)):
                if i != 0 and digitString[i] != digitString[i-1]:
                    ret += str(i - start) 
                    ret += digitString[start]
                    start = i
            ret += str(len(digitString) - start)
            #print('start = ', len(digitString) - start)
            ret += digitString[start]
            return ret
    
    def countAndSay(self, n: int) -> str:
        digitString = ""
        for i in range(1, n + 1):
            digitString = self.generate(i, digitString)
            print(i, digitString)
        return digitString