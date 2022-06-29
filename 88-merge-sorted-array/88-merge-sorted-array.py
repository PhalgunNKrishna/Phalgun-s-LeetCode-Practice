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
            
            if p2 >= n or (p1 < m and nums1copy[p1] < nums2[p2]):
                nums1[p] = nums1copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1