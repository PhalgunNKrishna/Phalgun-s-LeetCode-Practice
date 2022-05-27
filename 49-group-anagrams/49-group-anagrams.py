class Solution:
    
    ### APPROACH 1:
    #       Sort the items in the given list of strings because a group of anagrams that are sorted would all have the same sorted value.
    def droupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sortedStrings = {}
        
        for i in strs:
            sortStr = "".join(sorted(i))
            if sortStr in sortedStrings:
                li = list(sortedStrings[sortStr])
                li.append(i)
                sortedStrings[sortStr] = tuple(li)
            else:
                sortedStrings[sortStr] = tuple([i])
                
        print('sorted strings = ', sortedStrings)
        
        ret = []
        
        for i in sortedStrings.values():
            ret.append(list(i))
            
        print('ret = ', ret)    
        return ret
    
    
    ### APPROACH 2:
    #       Make a character count for each of the strings given. if the character count matches the current string iteration, append it to the dict's value associated with the character count
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        characterCount = {}
    
        for s in strs:
            count = []
            for c in sorted(s):
                print('sorted = ', sorted(s))
                count.append(ord(c) - ord('a') + 1)
            if tuple(count) in characterCount:
                anagrams = list(characterCount[tuple(count)])
                anagrams.append(s)
                characterCount[tuple(count)] = anagrams
            else:
                characterCount[tuple(count)] = tuple([s])
        print('character count = ', characterCount)
        
        ret = []
        
        for vals in characterCount.values():
            ret.append(vals)
            
        return ret