# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        if not root:
            return []
        q.append(root)
        result = []
        while q:
            curr_result = []
            for _ in range(len(q)):
                curr = q.popleft()
                curr_result.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            result.append(curr_result[-1])
        return result

                