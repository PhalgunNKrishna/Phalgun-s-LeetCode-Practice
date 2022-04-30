class Solution:
    
    ##### VIEW THIS AGAIN TONIGHT AND TOMORROW
    ##### MAKE SURE TO UNDERSTAND

    def expandAroundCenter(self, s, start, end):
        
        while (start >= 0 and end < len(s) and s[start] == s[end]):
            start -= 1
            end += 1
        
        return end - start - 1
        
    
    def longestPalindrome(self, s: str) -> str:
        
        if s == None or len(s) == 0:
            return ''
        
        start = 0
        end = 0
        
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i+1)
            length = max(len1, len2)
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2
                # print(start, end)
        return s[start: end+1]