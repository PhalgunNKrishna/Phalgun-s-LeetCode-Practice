class Solution:
    
    maxSubArray = []
    maxSum = 'a'
    
    # Divide and Conquer Like this Won't Bring About all the subArrays
    def updateMax(self, currSum, currLi):
        if self.maxSum == 'a' or currSum > self.maxSum:
            self.maxSum = currSum
            self.maxSubArray = currLi
        return
    
    def generateSubArrays(self, li):
        print('li = ', li)
        if (len(li) == 1):
            self.updateMax(li[0], li)
            return
        else:
            currSum = 0
            for i in li:
                currSum += i
            self.updateMax(currSum, li)
            midPoint = len(li) // 2
            self.generateSubArrays(li[0: midPoint])
            self.generateSubArrays(li[midPoint: len(li)])
            
        
    def amaxSubArray(self, nums: List[int]) -> int:
        self.generateSubArrays(nums)
        
        return self.maxSum
    
    def bmaxSubArray(self, nums: List[int]) -> int:
        
        maximumSum = -math.inf
        
        for i in range(len(nums)):
            currSum = 0
            for j in range(i, len(nums)):
                currSum += nums[j]
                maximumSum = max(currSum, maximumSum)
                
        return maximumSum
    
    def maxSubArray(self, nums: List[int]) -> int:
        
        currSub = nums[0]
        maxSub = nums[0]
        
        for i in range(1, len(nums)):
            if currSub < 0:
                currSub = nums[i]
            else:
                currSub += nums[i]
            maxSub = max(currSub, maxSub)
            print(maxSub, currSub, i)
            
        return maxSub
        