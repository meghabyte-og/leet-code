class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        adj = dict()
        for i in range(numCourses):
            adj[i] = []
        for i,j in pre:
            adj[i].append(j)
        visited = set()
        curr_path = set()
        def dfs(node):
            visited.add(node)
            curr_path.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    curr_path.add(neighbor)
                    ans = dfs(neighbor)
                    if ans == False:
                        return False
                    curr_path.remove(neighbor)
                elif neighbor in visited and neighbor in curr_path:
                    return False
            return True
        
        for i in range(numCourses):
            if i not in visited:
                curr_path.add(i)
                visited.add(i)
                ans = dfs(i)
            if not ans:
                return False
            if i in curr_path:
                curr_path.remove(i)
        return True
        

                