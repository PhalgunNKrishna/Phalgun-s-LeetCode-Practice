class Solution:
    
    # GREEDY
    def jump(self, nums: List[int]) -> int:
        
        numJumps = 0
        currJumpEnd = 0
        farthest = 0
        
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == currJumpEnd:
                numJumps += 1
                currJumpEnd = farthest
        return numJumps
    
    # GOT ANSWER CORRECT! 
    ### But Time Limit exceeded at test case 73 / 109
    def attempt1(self, nums: List[int]) -> int:
        
        jumpsList = []
        
        def jumpCombos(currIndex, currJumps, jumpVal):
            if currIndex == len(nums) - 1:
                jumpsList.append(currJumps)
                return
            elif currIndex >= len(nums):
                return
            elif nums[currIndex] == 0:
                return
            elif jumpVal == 0:
                return
            else:
                for i in range(nums[currIndex] + 1):
                    jumpCombos(currIndex + i, currJumps + 1, i)
            
        jumpCombos(0, 0, -1)
        
        jumpsList.sort()
        
        return jumpsList[0]