class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans

            if not node:
                return -1, -1

            leftLeft, leftRight = dfs(node.left)
            rightLeft, rightRight = dfs(node.right)

            left = leftRight + 1
            right = rightLeft + 1
            ans = max(ans, left, right)
            return left, right

        dfs(root)
        return ans