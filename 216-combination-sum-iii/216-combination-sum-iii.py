class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        results = []
        
        def backtrack(currSum, currCombo, next_start):
            
            if currSum == n and len(currCombo) == k:
                results.append(list(currCombo))
                return
            
            elif currSum > n or len(currCombo) == k:
                return

            for i in range(next_start, 9):
                currCombo.append(i+1)
                backtrack(currSum+i+1, currCombo, i+1)
                currCombo.pop()

        backtrack(0, [], 0)

        return results           