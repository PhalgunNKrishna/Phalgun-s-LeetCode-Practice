# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        visited = set()
        duplicates = set()
        
        if head == None or head.next == None:
            return head
        
        liNode = head
        
        while head != None:
            print('here = ', head.val)
            if head.val in visited:
                duplicates.add(head.val)
            visited.add(head.val)
            head = head.next
            
        print('dup = ', duplicates)
        
        head = liNode
        
        while head and head.val in duplicates:
            head = head.next
            
        liNode = head
        
        if liNode == None or liNode.next == None:
            return liNode
            
        print('head val = ', head.val)
        
        while head != None:
            nextNode = head.next
            while nextNode and nextNode.val in duplicates:
                nextNode = nextNode.next
            head.next = nextNode
            head = head.next
                
                
        return liNode