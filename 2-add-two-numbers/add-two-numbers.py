# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1=0
        n2=0
        i=0
        while l1:
            n1+=l1.val*(10**i)
            l1=l1.next
            i=i+1
        i=0
        while l2:
            n2+=l2.val*(10**i)
            l2=l2.next
            i=i+1
        ans=str(n1+n2)
        current=ListNode(int(ans[::-1][0]))
        head=current
        for i in ans[::-1][1:]:
            node = ListNode(int(i))
            head.next = node
            head = head.next
        
        return current




            