class Solution:
    def combinationSum2Attempt1(self, candidates: List[int], target: int) -> List[List[int]]:
        
        combinations = []
        
        def comboGen(currSum, currCombo, candCount):
            if currSum == target:
                if sorted(currCombo) not in combinations:
                    print('a = ', currCombo)
                    combinations.append(list(sorted(currCombo)))
                return 
            elif currSum > target:
                return
            else:
                for i in candidates:
                    exists = candCount[i]
                    if exists:
                        currCombo.append(i)
                        copyCount = dict(candCount)
                        copyCount[i] = copyCount[i] - 1
                        comboGen(currSum + i, currCombo, copyCount)
                        currCombo.pop()
        
        # creating candidate count table
        candidatesCount = dict()
        for i in candidates:
            if i not in candidatesCount:
                candidatesCount[i] = 1
            else:
                candidatesCount[i] += 1
        print(candidatesCount)
        
        comboGen(0, [], candidatesCount)
        
        return combinations
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(comb, remain, curr, counter, results):
            if remain == 0:
                # make a deep copy of the current combination
                #   rather than keeping the reference.
                results.append(list(comb))
                return
            elif remain < 0:
                return

            for next_curr in range(curr, len(counter)):
                candidate, freq = counter[next_curr]

                if freq <= 0:
                    continue

                # add a new element to the current combination
                comb.append(candidate)
                counter[next_curr] = (candidate, freq-1)

                # continue the exploration with the updated combination
                backtrack(comb, remain - candidate, next_curr, counter, results)

                # backtrack the changes, so that we can try another candidate
                counter[next_curr] = (candidate, freq)
                comb.pop()

        results = []  # container to hold the final combinations
        counter = Counter(candidates)
        print('counter 1 = ', counter)
        # convert the counter table to a list of (num, count) tuples
        counter = [(c, counter[c]) for c in counter]
        print('counter 2 = ', counter)

        backtrack(comb = [], remain = target, curr = 0,
                  counter = counter, results = results)

        return results