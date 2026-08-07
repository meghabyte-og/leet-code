class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj = dict()
        n = len(isConnected)
        for i in range(n):
            adj[i] = []
            for j in range(n):
                if i == j:
                    continue
                if isConnected[i][j] == 1:
                    adj[i].append(j) 

        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)
            return
        
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        return count
            
            

        

                
