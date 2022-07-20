# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # MY SOLUTION
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        sortedList = []
        
        while head != None:
            sortedList.append(head.val)
            head = head.next
        
        # print(sortedList)
        
        def createRoot(sortedList):
            
            if not len(sortedList):
                return None
            
            rootIndex = (len(sortedList) - 1) // 2
            rootVal = sortedList[rootIndex]
            
            print(rootVal)
            print(sortedList[:rootIndex])
            print(sortedList[rootIndex + 1:])
            print('---')
            
            root = TreeNode(rootVal)
            root.left = createRoot(sortedList[:rootIndex])
            root.right = createRoot(sortedList[rootIndex + 1:])
            
            return root
        
        return createRoot(sortedList)
        