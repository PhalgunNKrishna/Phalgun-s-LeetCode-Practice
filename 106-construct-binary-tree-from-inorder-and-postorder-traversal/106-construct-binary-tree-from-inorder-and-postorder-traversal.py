# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        inorderMap = {}
        
        for index, value in enumerate(inorder):
            inorderMap[value] = index
            
        print(inorderMap)
            
        def createRoot(left, right):
            
            if left > right:
                return None
            
            rootVal = postorder.pop()
            rootIndex = inorderMap[rootVal]
            
            root = TreeNode(rootVal)
            root.right = createRoot(rootIndex + 1, right)
            root.left = createRoot(left, rootIndex - 1)
            
            return root
            
        return createRoot(0, len(inorder) - 1)