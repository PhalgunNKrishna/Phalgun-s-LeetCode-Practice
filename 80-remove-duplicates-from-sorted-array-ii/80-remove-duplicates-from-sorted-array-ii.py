class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        instances = {}
        
        copy = list(nums)
        
        for i in range(len(nums)):
            if nums[i] in instances.keys() and instances[nums[i]] == 2:
                # nums.pop(i)
                continue
            elif nums[i] not in instances.keys():
                instances[nums[i]] = 1
            else:
                instances[nums[i]] = instances[nums[i]] + 1
                
        print('instances = ', instances)
        
        iteration = 0
        for i in instances.keys():
            print(i, instances[i])
            for j in range(1, instances[i] + 1):
                nums[iteration] = i
                iteration += 1
        
        k = 0
        for val in instances.values():
            k += val
            
        return k