class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        adj = {}
        for node in range(n):
            adj[node] = []
            for connection in range(n):
                if node == connection: 
                    continue
                if isConnected[node][connection] == 1:
                    adj[node].append(connection)
        
        print(adj)

        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        count = 0

        for i in range(len(isConnected)):
            if i not in visited:
                count += 1
                dfs(i)
        
        return count