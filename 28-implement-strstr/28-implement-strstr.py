class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle) == 0:
            return 0
        
        for i in range(len(haystack) - len(needle) + 1):
            foundNeedle = True
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    foundNeedle = False
                    break
            if foundNeedle:
                return i
        return -1