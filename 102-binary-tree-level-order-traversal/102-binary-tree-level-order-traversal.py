# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        levels = []
        
        if not root:
            return levels
        
        def iterate(node, level):
            
            if len(levels) == level:
                levels.append([])
                
            levels[level].append(node.val)
            
            if node.left:
                iterate(node.left, level + 1)
                
            if node.right:
                iterate(node.right, level + 1)
                
        iterate(root, 0)
        
        return levels