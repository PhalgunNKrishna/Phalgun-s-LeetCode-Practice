# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    preOrderIndex = 0
    
    def abuildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        root = TreeNode(preorder[0])
        rootIndex = 'a'
        
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                rootIndex = i
                
        print('root = ', rootIndex)
                
        root.left = self.buildTree(preorder[1:], inorder[:rootIndex])
        root.right = self.buildTree(preorder[1:], inorder[rootIndex + 1:])
        
        return root
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorderMap = {}
        
        for index, value in enumerate(inorder):
            inorderMap[value] = index
        
        def arrayToTree(left, right):
            # no elements to construct the tree
            if left > right: return None
            
            rootVal = preorder[self.preOrderIndex]
            root = TreeNode(rootVal)
            
            self.preOrderIndex += 1
            
            root.left = arrayToTree(left, inorderMap[rootVal] - 1)
            root.right = arrayToTree(inorderMap[rootVal] + 1, right)
            
            return root
            
        return arrayToTree(0, len(preorder) - 1)