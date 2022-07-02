# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    ### FAIRLY CLOSE
    def areverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        stack = []
        inStack = False
        
        ret = head
        leftPtr = head
        
        while head != None:
            
            print(head.val)
            
            if head.val == left:
                inStack = True
                stack.append(head.val)
                head = head.next
            elif head.val == right:
                inStack = False
                stack.append(head.val)
                head = head.next
            elif inStack:
                stack.append(head.val)
                head = head.next
            else:
                print('val = ', leftPtr.val)
                if leftPtr != head:
                    leftPtr.next = head
                leftPtr = head
                head = head.next
        
        print(stack)
        
        final = ret
        
        while len(stack):
            ret.next = ListNode(stack.pop())
            ret = ret.next
            print('ret val = ', ret.val)
            
        return final
    
    ### LOOK AT LATER
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        # Empty list
        if not head:
            return None

        # Move the two pointers until they reach the proper starting point
        # in the list.
        cur, prev = head, None
        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m - 1, n - 1

        # The two pointers that will fix the final connections.
        tail, con = cur, prev

        # Iteratively reverse the nodes until n becomes 0.
        while n:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1

        # Adjust the final connections as explained in the algorithm
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head