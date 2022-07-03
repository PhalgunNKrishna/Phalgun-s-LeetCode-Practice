# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def generate(start, end):
            
            if start > end:
                return [None,]
            
            allTrees = []
            
            for i in range(start, end + 1):
                leftTrees = generate(start, i - 1)
                rightTrees = generate(i + 1, end)
                
                for l in leftTrees:
                    for r in rightTrees:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        allTrees.append(currTree)
                        
            return allTrees
            
        if n:
            return generate(1, n)
        
        return []