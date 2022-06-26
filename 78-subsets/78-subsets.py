class Solution:
    
    # SOLUTION USES BACKTRACKING (.pop())
    # DON'T LOOP OVER THE ELEMENTS OF NUMS, LOOP OVER THE POSSIBLE LENGTHS OF THE COMBOS (0, 1, 2, ...)   
    # TIMELIMIT EXCEEDED
    def asubsets(self, nums: List[int]) -> List[List[int]]:
        
        allCombos = []
        
        def generateSets(currCombo, currSize):
            
            if len(currCombo) == currSize:
                # WHEN SHOULD YOU HAVE TO MAKE A DEEP COPY?
                if sorted(currCombo) not in allCombos:
                    allCombos.append(sorted(list(currCombo)))
                return
            for i in nums:
                if i not in currCombo:
                    currCombo.append(i)
                    generateSets(currCombo, currSize)
                    currCombo.pop()
                
        for i in range(len(nums) + 1):
            generateSets([], i)
            
        return allCombos
    
    # 2nd TRY
    # BASICALLY SAME AS ABOVE BUT WITH MINOR ALTERATION ("FIRST" ARGUMENT HELPS TO NOT HAVE TO CHECK IF CURRENT ELEMENT ALREADY IN CURRCOMBO)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        allCombos = []
        
        def generateSets(currCombo, currSize, first = 0):
            
            if len(currCombo) == currSize:
                # WHEN SHOULD YOU HAVE TO MAKE A DEEP COPY?
                if sorted(currCombo) not in allCombos:
                    allCombos.append(sorted(list(currCombo)))
                return
            for i in range(first, len(nums)):
                currCombo.append(nums[i])
                generateSets(currCombo, currSize, i + 1)
                currCombo.pop()
                
        for i in range(len(nums) + 1):
            generateSets([], i)
            
        return allCombos