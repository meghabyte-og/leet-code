import math
from collections import deque
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def bfs(graph,source)->int:
            q=deque()
            maxlen=1
            visited={}
            visited[source]=None
            q.append(source)
            while q:
                curr=q.popleft()
                maxlen+=1
                for i in graph[curr]:
                    if i not in visited:
                        visited[i]=None
                        q.append(i)
            return maxlen





        adj={}
        for i in range(len(bombs)):
            for j in range(i+1,len(bombs)):
                if i not in adj:
                    adj[i]=[]
                if j not in adj:
                    adj[j]=[]
                dist=math.sqrt((bombs[i][0]-bombs[j][0])**2 + (bombs[i][1]-bombs[j][1])**2)
                # if abs(bombs[i][2]-bombs[j][2])<=dist and dist<=bombs[i][2]+bombs[j][2]:
                if dist<=bombs[i][2]:
                    adj[i].append(j)
                if dist<=bombs[j][2]:
                    adj[j].append(i)
        print(adj)
        length=0
        # for i in adj:
        #     if len(adj[i])>maxlen:
        #         maxlen=len(adj[i])
        # return maxlen+1
        visited={}
        q=deque()

        for i in adj:
            curr_len=bfs(adj,i)
            if curr_len>length:
                length=curr_len
        return abs(length-1)
            

