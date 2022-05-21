class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        permutations = []
        
        def createPermutations(currPerm):
            print('currPerm = ', currPerm)
            if len(currPerm) == len(nums):
                print('here')
                permutations.append(list(currPerm))
                return
            elif len(currPerm) > len(nums):
                return
            else:
                for i in nums:
                    if i not in currPerm:
                        print('ab')
                        currPerm.append(i)
                        createPermutations(currPerm)
                        currPerm.pop()
        
        createPermutations([])
        
        return permutations