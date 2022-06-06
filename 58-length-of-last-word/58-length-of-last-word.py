class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        li = s.split(' ')
        print(li)
        
        
        ### STUDY REVERSED FOR LOOP RANGE
        for i in range(len(li) - 1, -1, -1):
            print(li[i])
            if len(li[i]):
                return len(li[i])