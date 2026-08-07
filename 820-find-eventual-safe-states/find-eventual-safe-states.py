class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = set()
        currpath = set()

        def dfs(node: int) -> bool:
            visited.add(node)
            currpath.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    ans = dfs(neighbor)
                    if ans == True:
                        return True
                else : #neighbor is not in visited
                    if neighbor in currpath:
                        return True

            currpath.remove(node)
            return False
        result = []
        for i in range(len(graph)):
            if i not in visited:
                ans = dfs(i)
        
        for i in range(len(graph)):
            if i not in currpath:
                result.append(i)
        return result