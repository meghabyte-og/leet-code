class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adj = {}

        for i,j in edges:
            if i not in adj:
                adj[i] = []
            if j not in adj:
                adj[j] = []
            adj[j].append(i)
            adj[i].append(j)

        n = len(adj)       

        for node in adj:
            if len(adj[node]) == n-1:
                return node
        
        

