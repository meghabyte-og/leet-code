class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        currpath = []
        def dfs(node):
            currpath.append(node)
            if node == len(graph) - 1:
                result.append(currpath.copy())
            
            for neighbor in graph[node]:
                dfs(neighbor)
            
            currpath.pop()
        
        dfs(0)
        return result