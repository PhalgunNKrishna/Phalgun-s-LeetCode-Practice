"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        
        Q = collections.deque([root])
        
        while Q:
            
            size = len(Q)
            
            for i in range(size):
                
                node = Q.popleft()
                
                # IMPORTANT CHECK
                # The queue will
                # contain nodes from 2 levels at most at any
                # point in time. This check ensures we only 
                # don't establish next pointers beyond the end
                # of a level
                if i < size - 1:
                    node.next = Q[0]
                    
                # add children to back of queue
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
                    
        return root