# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, currsum):
            if node is None:
                return 0
            currsum = currsum + node.val
            if currsum == targetSum:
                count = 1
            else:
                count = 0
            # print(currsum, node.val)
            return count + dfs(node.left, currsum)+dfs(node.right, currsum)


            
        def alsodfs(root):
            if root is None:
                return 0
            return dfs(root, 0) + alsodfs(root.left) + alsodfs(root.right)
        return alsodfs(root)

            
            
                