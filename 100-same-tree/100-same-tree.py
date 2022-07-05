# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    ## VERY CLOSE
    def aisSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        pTraverse = []
        qTraverse = []
        
        def inOrderTraverse(root, pTrav = True):
            
            if root:
                inOrderTraverse(root.left, pTrav)
                pTraverse.append(root.val) if pTrav else qTraverse.append(root.val)
                inOrderTraverse(root.right, pTrav)
                
        inOrderTraverse(p)
        
        inOrderTraverse(q, False)
        
        print(pTraverse, qTraverse)
        
        return pTraverse == qTraverse
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p == None and q == None:
            return True
        
        if p == None or q == None:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)