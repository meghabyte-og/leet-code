class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = [0] * n
        for i,j in trust:
            adj[i-1] += 1
            adj[j-1] -= 1
        for i in range(len(adj)):
            if adj[i] == -(n-1):
                return i+1
        return -1