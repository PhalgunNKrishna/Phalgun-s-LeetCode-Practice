class Solution:
    
    ### CLOSE
    def aMerge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        ret = []
        i = 0
        
        ### LOOK THiS UP LATER
        intervals.sort(key=lambda x: x[0])
        
        while i < len(intervals):
            print(ret, intervals)
            if i != len(intervals) - 1:
                if intervals[i][1] >= intervals[i+1][0]:
                    newInter = [intervals[i][0], max(intervals[i+1][1], intervals[i][1])]
                    ret.append(newInter)
                    intervals.pop(i+1)
                    intervals[i] = newInter
                    i += 1
                else:
                    ret.append(intervals[i])
                    i += 1
            else:
                ret.append(intervals[i])
                i += 1
            
        return ret
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        ret = []
        
        ### LOOK THiS UP LATER
        intervals.sort(key=lambda x: x[0])
        
        ret.append(intervals[0])
        
        for i in range(1, len(intervals)):
            if ret[-1][1] >= intervals[i][0]:
                ret[-1][1] = max(ret[-1][1], intervals[i][1])
            else:
                ret.append(intervals[i])
                
        return ret
                