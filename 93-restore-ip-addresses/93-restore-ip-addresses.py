class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        def valid(segment):
            
            ### helper function to check if segment meets conditions:
            ###     1. segment <= 255 and doesn't start with '0' --> ex) 051 starts with '0'
            ###     2. if it does start wit '0', make sure the segment length is 1 --> ex) segment HAS To be '0'
            print('seg = ', segment)
            if segment[0] == '0':
                if len(segment) == 1:
                    return True
                else:
                    return False
            else:
                return int(segment) <= 255
            
        def updateOutput(currPos):
            
            ### check if segment valid and append to list of valid IPs
            
            segment = s[currPos+1 : len(s)]
            
            if valid(segment):
                segments.append(segment)
                output.append('.'.join(segments))
                segments.pop()
                
        def backtrack(prev = -1, dots = 3):
            
            ### prev = position of previously placed dot
            
            for currPos in range(prev + 1, min(len(s) - 1, prev + 4)):
                segment = s[prev + 1: currPos + 1]
                if valid(segment):
                    segments.append(segment)
                    if dots - 1 == 0:
                        updateOutput(currPos)
                    else:
                        backtrack(currPos, dots - 1)
                    segments.pop()
                    
        output = []
        segments = []
        backtrack()
        
        return output
            
            