# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        visited = set()
        liNode = head
        prior = None
        
        while head != None:
            if head.val in visited:
                print('head vis = ', head.val, prior.val)
                prior.next = None
                head = head.next
            else:
                print('head = ', head.val, prior)
                visited.add(head.val)
                if prior:
                    prior.next = head
                prior = head
                head = head.next
        
        print('visited = ', visited)
        return liNode