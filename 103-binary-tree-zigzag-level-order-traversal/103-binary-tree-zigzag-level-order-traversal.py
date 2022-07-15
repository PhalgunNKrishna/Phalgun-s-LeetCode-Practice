# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    ### CLOSE
    def azigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        levels = []
        
        def helper(node, left, currLevel):
            
            if len(levels) == currLevel and node:
                levels.append([])
                
            if left:
                if node:
                    print('left = ', left, node.val)
                    levels[currLevel].append(node.val)
                    helper(node.right, False, currLevel + 1)
                    helper(node.left, True, currLevel + 1)
                
            else:
                if node:
                    print('left = ', left, node.val)
                    levels[currLevel].append(node.val)
                    helper(node.left, True, currLevel + 1)
                    helper(node.right, False, currLevel + 1) 
                
        helper(root, True, 0)
        
        return levels
    
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ret = []
        levelList = deque()
        
        if root is None:
            return []
        
        nodeQueue = deque([root, None])
        goLeft = True
        
        while len(nodeQueue):
            
            currNode = nodeQueue.popleft()
            
            if currNode:
                if goLeft:
                    levelList.append(currNode.val)
                else:
                    levelList.appendleft(currNode.val)
                    
                if currNode.left:
                    nodeQueue.append(currNode.left)
                if currNode.right:
                    nodeQueue.append(currNode.right)
            else:
                ret.append(levelList)
                
                if len(nodeQueue) > 0:
                    nodeQueue.append(None)
                    
                levelList = deque()
                goLeft = not goLeft
                
        return ret