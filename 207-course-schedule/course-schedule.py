class Solution:
    def canFinish(self, numCourses: int, prerequisites : List[List[int]]) -> bool:
        adj = dict()
        for i in range(numCourses):
            adj[i] = []
        for i,j in prerequisites :
            if i == j:
                return False
            adj[i].append(j)
        
        visited = set()
        currpath = set()
        def dfs(node):
            visited.add(node)
            currpath.add(node)

            for i in adj[node]:
                if i not in visited:
                    ans = dfs(i)
                    if ans == False:
                        return False
                else: #i s in visited
                    if i in currpath: #i is in visited and currpath
                        return False                    
            currpath.remove(node)
            return True
        

        for i in range(numCourses):
            if i not in visited:
                ans = dfs(i)
                if ans == False:
                    return False
        return True

        
        