class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        def dfs(node, parent):
            depth = 0
            for nei in tree[node]:
                if nei != parent:
                    depth = max(depth, dfs(nei, node))
            return depth + 1

        tree = {}
        for u,v in edges:
            if u not in tree:
                tree[u] = []
            if v not in tree:
                tree[v] = []
            tree[u].append(v)
            tree[v].append(u)
        return (2**(dfs(1, -1)-2))%(10**9 + 7)
        