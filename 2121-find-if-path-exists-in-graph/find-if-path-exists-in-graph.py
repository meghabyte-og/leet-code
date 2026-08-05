class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = dict()
        for i in range(n):
            adj[i] = [] 
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        dfs(source)
        return destination in visited
            