# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj = dict()
        def build_adj(node):
            if not node:
                return

            if node.val not in adj:
                adj[node.val] = []

            if node.left:
                adj[node.val].append(node.left.val)
                if node.left.val not in adj:
                    adj[node.left.val] = []
                adj[node.left.val].append(node.val)

            if node.right:
                adj[node.val].append(node.right.val)
                if node.right.val not in adj:
                    adj[node.right.val] = []
                adj[node.right.val].append(node.val)
                
            build_adj(node.left)
            build_adj(node.right)

        build_adj(root)
 
        q =deque()
        visited = set()

        q.append(target.val)
        visited.add(target.val)
        
        path = []
        
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if k == 0:
                    path.append(curr)
                for neighbor in adj[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)  
            k -= 1
        
        return path




