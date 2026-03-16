from collections import defaultdict
from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if len(edges)==0:
            return True
        graph=defaultdict(list)
        for edge in edges:
            # if edge[0] not in graph:
            #     graph[edge[0]]=[]
            graph[edge[0]].append(edge[1])
            # if edge[1] not in graph:
            #     graph[edge[1]]=[]
            graph[edge[1]].append(edge[0])  
        visited=set()

        #-----------------------BFS--------------------
        path=deque()
        path.append(source)
        while len(path)>0:


            curr=path.popleft()

            # check if visited 
            # if curr in visited:
            #     continue
            visited.add(curr)


            #check if destination is reached
            if curr==destination:
                return True


            #loop
            for i in graph[curr]:
                if i not in visited:
                    path.append(i)
        return False

        #------------------------DFS--------------------
        # stack=[source]
        # while len(stack)>0:
        #     curr=stack.pop()
        #     if curr==destination:
        #         return True
        #     if curr in visited: 
        #         continue
        #     visited.append(curr)
        #     for i in graph[curr]:
        #         stack.append(i)
        # return False
