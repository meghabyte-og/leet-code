# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        if head.next is None:
            return head
        count=0
        move=head
        while move:
                move=move.next
                count+=1
        for i in range(k%count if k>=count else k):
            temp=head
            while temp:
                if temp.next is None:
                    temp.next=head
                    head=temp
                    curr.next=None
                    
                    break
                curr=temp
                temp=temp.next
        return head
                    