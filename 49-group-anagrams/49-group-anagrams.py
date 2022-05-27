class Solution:
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
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