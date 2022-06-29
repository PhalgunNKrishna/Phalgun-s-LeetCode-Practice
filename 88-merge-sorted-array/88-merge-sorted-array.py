class Solution:

    ### NAIVE APPROACH
    def amerge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        for _ in range(len(nums1) - m):
            nums1.pop()
        
        for i in range(n):
            nums1.append(nums2[i])
            
        print(nums1)
        
        nums1.sort()
        
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        nums1copy = nums1[:m]
        
        p1 = 0
        p2 = 0
        
        for p in range(n + m):
            
            ### p2 >= n means the pointer has already gone through the entire num2 list since there's only n items in nums2
            ### p1 < m means that we haven't fully iterated through nums1copy yet
            ### since nums1copy is just the original nums1, we can check to see which of the elements pointed at are smaller and change up nums1 accordingly
            if p2 >= n or (p1 < m and nums1copy[p1] < nums2[p2]):
                nums1[p] = nums1copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1