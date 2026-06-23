class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected) 
        adj = []
        print(adj)
        for i in range(n):
            curr = []
            for j in range(len(isConnected[i])):
                if i == j :
                    continue
                if isConnected[i][j] == 1:
                    curr.append(j)
            adj.append(curr)

        visited = set()
        def dfs(curr):
            nonlocal visited
            if curr in visited:
                return 
            visited.add(curr)
            for neighbor in adj[curr]:
                dfs(neighbor)
        result = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                result += 1
        return result


        
                
