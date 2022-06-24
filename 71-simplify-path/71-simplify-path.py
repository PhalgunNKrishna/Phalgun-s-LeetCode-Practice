class Solution:
    def simplifyPath(self, path: str) -> str:
        
        pathLi = path.split('/')
        canon = '/'
        pathStack = []
        
        print('p = ', pathLi)
            
        for path in pathLi:
            if path == '..':
                if len(pathStack):
                    pathStack.pop()
                else:
                    continue
            elif path == '.':
                continue
            elif len(path):
                print('here = ', path)
                pathStack.append(path)
        
        print(pathStack)
        
        for path in pathStack:
            canon += (path + '/')
        
        if len(canon) > 1:
            return canon[:len(canon) - 1]
        
        return canon
