# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        q=deque()
        q.append(root)
        count=0
        while q:
            curr=q.popleft()
            
            if curr is None:
                break

            count+=1
            q.append(curr.left)
            q.append(curr.right)
        return count

