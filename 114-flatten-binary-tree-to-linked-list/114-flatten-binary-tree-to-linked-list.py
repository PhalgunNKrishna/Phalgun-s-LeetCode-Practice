# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def flattenTree(self, node):
        
        # Base Case #1: if no node
        if not node:
            return None
        
        # Base Case #2: if node is a leaf node
        if not node.left and not node.right:
            return node
        
        # Recursively flatten out left and right subtrees
        leftTail = self.flattenTree(node.left)
        rightTail = self.flattenTree(node.right)
        
        # set up connections
        if leftTail:
            leftTail.right = node.right
            node.right = node.left
            node.left = None
            
        if rightTail:
            return rightTail
        
        return leftTail
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        self.flattenTree(root)