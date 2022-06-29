# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    ### VERY CLOSE TO THE SOLUTION GIVEN (2 POINTER SOLUTION)
    def apartition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        lessThan = head
        greatThan = head
        ret = head
        
        while head != None:
            if head.val < x:
                if lessThan != head:
                    lessThan.next = head
                    lessThan = head
            else:
                if greatThan != head:
                    greatThan.next = head
                    greatThan = head
            
            head = head.next
            
        return ret
    
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        if head == None:
            return head
        
        if head.next == None:
            return head
        
        lessThan = ListNode(None)
        greatThan = ListNode(None)
        
        retLess = lessThan
        retGreat = greatThan
        
        while head != None:
            
            if head.val < x:
                if lessThan.val == None:
                    lessThan.val = head.val
                else:
                    lessThan.next = ListNode(head.val)
                    lessThan = lessThan.next
                print('less = ', lessThan)
            else:
                if greatThan.val == None:
                    greatThan.val = head.val
                else:
                    greatThan.next = ListNode(head.val)
                    greatThan = greatThan.next
                print('great = ', greatThan)
                    
            head = head.next
        
        if lessThan.val == None:
            return retGreat
        if greatThan.val == None:
            return retLess
        
        lessThan.next = retGreat
        
        return retLess