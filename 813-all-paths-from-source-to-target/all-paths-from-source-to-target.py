class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        currpath = []
        n = len(graph)
        def dfs(node):
            currpath.append(node)

            if node == n-1:
                result.append(currpath.copy())

            for i in graph[node]:
                dfs(i)     

            currpath.pop()
        dfs(0)
        return result