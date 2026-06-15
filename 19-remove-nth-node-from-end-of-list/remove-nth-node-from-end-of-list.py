# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        traverse = head
        count = 0
        if head.next is None:
            return head.next
        while traverse:
            traverse = traverse.next
            count += 1
        remove = head
        if n == count:
            head = head.next
            return head
        for i in range(count-n-1):
            remove = remove.next
        remove.next = remove.next.next
        return head