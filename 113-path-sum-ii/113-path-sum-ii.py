# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ret = []
        
        if not root:
            return ret
        
        def helper(node, currPath, currSum):
            
            if not node:
                return
            
            if currSum == targetSum and not node.left and not node.right:
                ret.append(list(currPath))
                return
            
            if currSum != targetSum and node.left is None and node.right is None:
                return

            if node.right and node.left:
                currPath.append(node.right.val)
                helper(node.right, currPath, currSum + node.right.val)
                currPath.pop()
                currPath.append(node.left.val)
                helper(node.left, currPath, currSum + node.left.val)
                currPath.pop()
                        
            elif node.right and not node.left:
                currPath.append(node.right.val)
                helper(node.right, currPath, currSum + node.right.val)
                currPath.pop()
                    
            elif not node.right and node.left:
                currPath.append(node.left.val)
                helper(node.left, currPath, currSum + node.left.val)
                currPath.pop()
        
        helper(root, [root.val], root.val)
        
        return ret
                        
                    
                