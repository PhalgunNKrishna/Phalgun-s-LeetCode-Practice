class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
    
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (high + low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        if low >= len(nums):
            return low
        if low < 0:
            return 0
        if nums[low] < target:
            return low + 1
        return low
    