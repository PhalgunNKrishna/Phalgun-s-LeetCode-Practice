# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    ### THOROUGHLY STUDY THIS --> MAKES SENSE NOW
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def generate(start, end):
            
            # generate(start, i - 1) --> end consistently decreasing by 1 --> if start > end, can't make a tree out of it
            # generate(i + 1, end) --> start consistently increasing by 1
            if start > end:
                return [None,]
            
            allTrees = []
            
            for i in range(start, end + 1):
                # left trees + right trees are the allTrees returned by generate() recursion
                leftTrees = generate(start, i - 1)
                rightTrees = generate(i + 1, end)
                
                # for each left tree, connect each of existing right trees to left tree through the current root
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