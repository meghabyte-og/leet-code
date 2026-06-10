# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaves(root, leaf):
            if not root:
                return
            if root.left is None and root.right is None:
                leaf.append(root.val)
            leaves(root.left, leaf)
            leaves(root.right,leaf)
            return leaf
        leaf1 = leaves(root1,[])
        leaf2 = leaves(root2, []) 
        if len(leaf1) != len(leaf2):
            return False
        for i in range(len(leaf1)):
            if leaf1[i] != leaf2[i]:
                return False
        return True

