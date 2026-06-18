# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0 
        def dfs(curr, maxval):
            if not curr:
                return 0
            count = 0
            if curr.val >= maxval:
                count = 1
            maxval = max(maxval, curr.val)
            count += dfs(curr.left, maxval)
            count += dfs(curr.right, maxval)
            return count
        return dfs(root, root.val)

                
            
            
            