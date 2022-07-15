# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        levels = []
        
        def helper(node, currLevel):
            
            if currLevel == len(levels):
                levels.append([])
            
            if node:
                levels[currLevel].append(node.val)
            
                if node.left:
                    helper(node.left, currLevel + 1)
                if node.right:
                    helper(node.right, currLevel + 1)
                    
            if levels[currLevel] == []:
                levels.pop()
                
        helper(root, 0)
        
        levels.reverse()
        
        return levels