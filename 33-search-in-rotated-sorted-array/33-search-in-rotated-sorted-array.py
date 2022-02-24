class Solution:
                           
    def search(self, nums: List[int], target: int) -> int:
        
        if target not in nums:
            return -1
        
        if len(nums) == 1:
            print('here')
            return 0
        
        pivot = self.findPivot(nums, target, 0, len(nums) - 1)
        print('pivot = ', pivot)
        
        # if target is smallest element
        if nums[pivot] == target:
            return pivot
        
        #if array is not rotated, search entire array
        if pivot == 0:
            return self.binSearch(nums, target, 0, len(nums) - 1)
        
        # search on right side
        if target < nums[0]:
            return self.binSearch(nums, target, pivot, len(nums) - 1)
        
        return self.binSearch(nums, target, 0, pivot)
        
    def findPivot(self, nums: List[int], target: int, left, right) -> int:
        
        
        if nums[left] < nums[right]:
            print('here = ', nums[left], nums[right])
            return 0
        
        while (left <= right):
            print('wakanda')
            pivot = (left + right) // 2
            if nums[pivot] > nums[pivot + 1]:
                return pivot + 1              
            else:
                if nums[pivot] < nums[left]:
                    right = pivot - 1
                else:
                    left = pivot + 1
                    
        return -1
            
        
    def binSearch(self, nums: List[int], target: int, left, right) -> int:
        
        while left <= right:
            mid = (left + right) // 2
            print('mid = ', mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        
        return -1