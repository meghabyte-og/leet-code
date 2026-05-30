# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # reverse first half
        if not head: 
            return 0
        if not head.next:
            return head.val
        if not head.next.next:
            return (head.val + head.next.val)
        total = 0
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            nextnode = slow.next
            slow.next = prev
            prev = slow
            slow = nextnode   
        head.next = slow 

        #prev = head of new LL
        fast = prev
        node = prev
        twin = prev
        while fast and fast.next:
            fast = fast.next.next
            twin = twin.next
        maxsum = 0
        while twin:
            maxsum = max(maxsum,(twin.val + node.val))
            twin = twin.next
            node = node.next
        return maxsum

       
        
        
        