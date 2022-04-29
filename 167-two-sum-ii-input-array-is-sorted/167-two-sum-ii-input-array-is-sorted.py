class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # ret = []
        
        low = 0
        high = len(numbers) - 1
        
        while low < high:
            currSum = numbers[low] + numbers[high]
            if currSum == target:
                return [low + 1, high + 1]
            elif currSum < target:
                low = low + 1
            else:
                high = high - 1
        
        return [-1, -1]
        
            