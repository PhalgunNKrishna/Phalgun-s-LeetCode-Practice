# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        pathSolns = []
        
        if not root:
            return False
        
        def helper(node, currSum):
            
            if currSum == targetSum and not node.left and not node.right:
                pathSolns.append(True)
                return
            
            elif currSum > targetSum and not node.left and not node.right:
                pathSolns.append(False)
                return
            
            else:
                if node and node.left:
                    helper(node.left, currSum + node.left.val) 
                if node and node.right:
                    helper(node.right, currSum + node.right.val)
                
        helper(root, root.val)
        
        if True in pathSolns:
            return True
        
        return False
             