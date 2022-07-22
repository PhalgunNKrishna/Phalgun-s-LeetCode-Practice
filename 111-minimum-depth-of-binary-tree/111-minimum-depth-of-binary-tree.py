# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # CLOSE
    def aminDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
    
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        children = [root.left, root.right]
        # if at leaf node
        if not any(children):
            return 1
        
        minDepth = float('inf')
        
        for c in children:
            if c:
                minDepth = min(self.minDepth(c), minDepth)
        
        return minDepth + 1