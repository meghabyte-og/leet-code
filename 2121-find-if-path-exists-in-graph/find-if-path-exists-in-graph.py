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
            if node == destination:
                return True
            for neighbor in adj[node]:
                if neighbor not in visited:
                    ans = dfs(neighbor)
                    if ans == True:
                        return True
            return False
        return dfs(source)
        