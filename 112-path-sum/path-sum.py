# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False 
        def dfs(node, currsum):
            currsum += node.val
            if not node.left and not node.right:
                if currsum == targetSum: 
                    return True
                return False
            right = False
            left = False
            if node.right:
                right = dfs(node.right, currsum)
            if node.left:
                left = dfs(node.left, currsum)
            return right or left
        return dfs(root, 0)
            

