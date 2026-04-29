# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        flag=0
        if head.next is None:
            return head.next
        while slow and slow.next and fast and fast.next:
            fast=fast.next.next
            if fast!=None and fast.next==None:
                slow.next=slow.next.next
                break
            if fast is None: 
                slow.next=slow.next.next
                break
            slow=slow.next
        return head

        

        
        
       