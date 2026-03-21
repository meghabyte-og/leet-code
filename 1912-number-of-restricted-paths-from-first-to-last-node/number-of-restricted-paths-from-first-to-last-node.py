import heapq
from collections import deque
class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        def dijkstra(graph,start):
            dist={i:float('inf') for i in graph}
            dist[start]=0
            heap=[(0,start)]
            while heap:
                curr_dist,curr_node=heapq.heappop(heap)
                if curr_dist>dist[curr_node]:
                    continue
                for neighbor, weight in graph[curr_node]:
                    if dist[curr_node]+weight<dist[neighbor]:
                        dist[neighbor]=dist[curr_node]+weight
                        heapq.heappush(heap,(dist[curr_node]+weight,neighbor))
            return dist
        adj={i+1:[] for i in range(n)}
        for i in edges:
            adj[i[0]].append([i[1],i[2]])
            adj[i[1]].append([i[0],i[2]])
        new_adj={i:[] for i in adj}
        d=(dijkstra(adj,n))
        for i in adj:
            for j in adj[i]:
                if d[i]>d[j[0]]:
                    new_adj[j[0]].append(i)
        print(new_adj)
        store={}
        def dp(x):
            if x==1:
                return 1
            if x in store:
                return store[x]
            paths=0
            for i in new_adj[x]:
                paths+=dp(i)
            store[x]=paths
            return paths
        return(dp(n)%(10**9+7))


        # def dfs(source,path):
        #     if source in path:
        #         return
        #     path.append(source)
        #     if source==n:
        #         paths.append(path[:])
        #         #return
        #     else:
        #         for i in adj[source]:
        #             dfs(i[0],path)
        #     path.pop()
        # dfs(1,[])
        # count=0
        # for p in paths:
        #     c=0
        #     for i in range(len(p)-1):
        #         if d[p[i]]<=d[p[i+1]]:
        #             break
        #         c=c+1
        #     if c==len(p)-1:
        #         # print(p)
        #         count=count+1                         
        # return count
                    
                
                
                    
                    

            
            
                



        

        
     