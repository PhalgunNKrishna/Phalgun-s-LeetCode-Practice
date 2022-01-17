class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        lower = self.findBound(nums, target, True)
        if lower == -1:
            return [-1, -1]
        
        upper = self.findBound(nums, target, False)
        if upper == -1:
            return [-1, -1]
        
        return [lower, upper]
        
    def findBound(self, nums: List[int], target: int, isLower: bool) -> int:
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            print(left, mid, right)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                if isLower:
                    if mid == left:
                        return mid
                    elif nums[mid - 1] != target:
                        return mid
                    else:
                        right = mid - 1
                else:
                    if mid == right:
                        return mid
                    elif nums[mid + 1] != target:
                        return mid
                    else:
                        left = mid  + 1
        return -1