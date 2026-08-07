class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        directed = {i: set() for i in range(n)}
        undirected = {i: set() for i in range(n)}

        for i,j in connections:
            directed[i].add(j)
            undirected[i].add(j)
            undirected[j].add(i)
        
        visited = set()
        count = [0]

        def dfs(node):
            visited.add(node)
            for neighbor in undirected[node]:
                if neighbor not in visited:
                    if neighbor in directed[node]:
                        count[0] +=1 
                    dfs(neighbor)
        dfs(0)
        return count[0]
        