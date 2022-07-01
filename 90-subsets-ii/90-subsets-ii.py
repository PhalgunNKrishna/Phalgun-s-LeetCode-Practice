class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        subsets = []
        
        def generateSet(currSet, expectedSize, iteration):
            
            if len(currSet) == expectedSize:
                if sorted(currSet) not in subsets:
                    subsets.append(sorted(list(currSet)))
                return
            else:
                for i in range(iteration, len(nums)):
                    currSet.append(nums[i])
                    generateSet(currSet, expectedSize, i + 1)
                    currSet.pop()
                    
        for i in range(len(nums) + 1):
            generateSet([], i, 0)
            
        return subsets
                