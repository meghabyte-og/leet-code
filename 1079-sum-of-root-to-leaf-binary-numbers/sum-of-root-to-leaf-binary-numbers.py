# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        b=''
        bins=[]
        def recurse(node,b):
            if node is None:
                return
            if node.left is None and node.right is None:
                b=b+str(node.val)
                bins.append(b)
                return
                
            b=b+str(node.val)
            recurse(node.left,b)
            recurse(node.right,b)
        
        def binsum(n):
            s=0
            for i in range(len(n)):
                s+=2**i * int(n[len(n)-i-1])
            return s
        recurse(root,'')
        s=0
        for i in bins:
            s+=binsum(i)
        return s