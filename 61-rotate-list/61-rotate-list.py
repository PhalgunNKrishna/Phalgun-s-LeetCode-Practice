# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    
    # SOLVED BUT EXCEEDED THE TIME LIMIT
    def arotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        rotationsLeft = k
        newTail = head
        currTail = head
        
        if head == None:
            return head
        
        if head.next == None:
            return head
        
        if head.next.next == None:
            while rotationsLeft:
                currTail = head.next
                currTail.next = head
                newTail.next = None
                head = currTail
                rotationsLeft -= 1
                newTail = head
                currTail = head
        
        while rotationsLeft:
            while newTail.next.next:
                newTail = newTail.next
                currTail = newTail.next
            currTail.next = head
            newTail.next = None
            head = currTail
            newTail = head
            rotationsLeft -= 1
            
        return head
    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    
        if not head:
            return None
        if not head.next:
            return head
        
        # close the ring and keep track of how many nodes in list. Close by making tail connect to head
        currTail = head
        nodeCount = 1
        while currTail.next:
            currTail = currTail.next
            nodeCount += 1
        currTail.next = head

        # new tail should be n - k % n - 1
        # new head should be n - k % n
        ###### WHY IS THE NEW HEAD AND NEW TAIL THESE POSITIONS THOUGH
        newTail = head
        for i in range(nodeCount - k % nodeCount - 1):
            newTail = newTail.next
        newHead = newTail.next
        
        # break the ring
        newTail.next = None
        
        return newHead