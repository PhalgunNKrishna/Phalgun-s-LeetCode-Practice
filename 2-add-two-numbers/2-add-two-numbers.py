# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head1 = l1
        head2 = l2
        
        l3 = ListNode()
        currHead = l3
        
        carry = 0
        
        while head1 != None or head2 != None:
            x = head1.val if head1 else 0
            y = head2.val if head2 else 0
            sum = x + y + carry 
            carry = sum // 10
            currHead.next = ListNode(sum % 10)
            currHead = currHead.next
            if head1 != None:
                head1 = head1.next
            if head2 != None:
                head2 = head2.next
            
        
        if carry > 0:
            currHead.next = ListNode(carry)
        
        return l3.next
            
            
        