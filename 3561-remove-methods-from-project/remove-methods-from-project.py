class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = dict()
        for i in range(n):
            adj[i] = []
        for i in invocations:
            adj[i[0]].append(i[1])

        visited = set()
        def dfs(k):
            visited.add(k)
            for neighbor in adj[k]:
                if neighbor not in visited:
                    dfs(neighbor)
        dfs(k)

        for i in invocations:
            if i[1] in visited and i[0] not in visited:
                return [i for i in range(n)]
            
        
        result = []
        for i in range(n):
            if i not in visited:
                result.append(i)
        return result






