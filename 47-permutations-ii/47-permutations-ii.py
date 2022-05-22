class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        permutations = []
        
        def generatePermutations(currPerm, visited):
            if len(currPerm) == len(nums) and currPerm not in permutations:
                permutations.append(list(currPerm))
                return
            elif len(currPerm) > len(nums):
                return
            else:
                for i in range(len(nums)):
                    if i not in visited:
                        currPerm.append(nums[i])
                        visited.append(i)
                        generatePermutations(currPerm, visited)
                        currPerm.pop()
                        visited.pop()
    
        generatePermutations([], [])
        
        return permutations