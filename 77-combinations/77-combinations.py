class Solution:
    
    combos = []
    
    def acombine(self, n: int, k: int) -> List[List[int]]:
        
        def createCombos(currCombo):
            
            if len(currCombo) == k and sorted(currCombo) not in self.combos:
                self.combos.append(currCombo)
            else:
                for i in range(1, n + 1):
                    if i not in currCombo:
                        currCombo.append(i)
                        createCombos(list(currCombo))
                        currCombo.pop()
                    
        createCombos([])
        
        return self.combos
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first = 1, curr = []):
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
            for i in range(first, n + 1):
                # add i into the current combination
                curr.append(i)
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        backtrack()
        return output