# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    ### CLOSE:
        # Issue: doesn't add "None" to the iteration list b/c:
        # if nodeA != None:
        # becomes an issue if one child of a node exists while the other doesn't
        
    def aisSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        left = []
        right = []
        
        def inOrder(nodeA):
            
            if nodeA != None:
                inOrder(nodeA.left)
                left.append(nodeA.val)
                inOrder(nodeA.right)
            
        def otherOrder(nodeB):
            
            if nodeB != None:
                otherOrder(nodeB.right)
                right.append(nodeB.val)
                otherOrder(nodeB.left)
                
        inOrder(root.left)
        otherOrder(root.right)
        
        print(left, right)
        
        return left == right
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isMirror(treeOne, treeTwo):
            
            if treeOne == None and treeTwo == None:
                return True
            
            if treeOne == None or treeTwo == None:
                return False
            
            return treeOne.val == treeTwo.val and isMirror(treeOne.left, treeTwo.right) and isMirror(treeOne.right, treeTwo.left)
        
        return isMirror(root.left, root.right)