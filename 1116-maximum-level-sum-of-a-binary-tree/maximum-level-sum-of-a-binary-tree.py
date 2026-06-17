# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxsum = -float('inf')
        level = 0
        q = deque()
        q.append(root)
        maxlevel = 0
        while q:
            curr_sum = -float('inf')
            level += 1

            for i in range(len(q)):
                curr = q.popleft()
                if i == 0:
                    curr_sum = curr.val
                else:
                    curr_sum += curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            # maxsum = max(maxsum, curr_sum)
            if curr_sum > maxsum :
                maxsum = curr_sum
                maxlevel = level
        return maxlevel
        