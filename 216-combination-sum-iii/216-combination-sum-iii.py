class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []
        def backtrack(currSum, currCombo, next_start):
            if currSum == n and len(currCombo) == k:
                # make a copy of current combination
                # Otherwise the combination would be reverted in other branch of backtracking.
                results.append(list(currCombo))
                return
            elif currSum > n or len(currCombo) == k:
                # exceed the scope, no need to explore further.
                return

            # Iterate through the reduced list of candidates.
            for i in range(next_start, 9):
                currCombo.append(i+1)
                backtrack(currSum+i+1, currCombo, i+1)
                # backtrack the current choice
                currCombo.pop()

        backtrack(0, [], 0)

        return results           