# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    ### IDEA:
        # inorder traveral of a BST will always be in ASCENDING ORDER
        # ==> b/c this is basically ascending except for in 2 spots, we can easily see which 2 elements need to be swapped after doing an inorder traversal
        # a/f finding the elements to be swapped, traverse again and swap the values u know need to be swapped
        
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        inOrder = []
        
        def traverseInOrder(root):
            
            if root != None:
                traverseInOrder(root.left)
                inOrder.append(root.val)
                traverseInOrder(root.right)
                
        def findSwapped(nums):
            
            x = None
            y = None
            
            
            ### IDEA:
            #       in list of numbers, first swapped element is element that is bigger than the element after it, hence you assign x to it and y to the element right after for now
            #       HOWEVER, the element right after may not be the other swapped element so you keep iterating through until you reach another element that is bigger than the element right after that one. THIS is the SECOND SWAPPED
            for i in range(len(nums) - 1):
                if nums[i + 1] < nums[i]:
                    y = nums[i + 1]
                    print(x, y)
                    if x is None:
                        x = nums[i]
                        print(x, y)
                    else:
                        break
            
            return x, y
        
        # count = 2 because, you have to recover 2 wrongly placed numbers
        def recover(r, count):
            
            if r:
                
                if r.val == x:
                    r.val = y
                    count -= 1
                    if count == 0:
                        return
                elif r.val == y:
                    r.val = x
                    count -= 1
                    if count == 0:
                        return
                    
                recover(r.left, count)
                recover(r.right, count)
                       
        traverseInOrder(root)
        
        print(inOrder)
        
        x, y = findSwapped(inOrder)
        
        recover(root, 2)
        
        
                
        