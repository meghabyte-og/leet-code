class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        istrusted=[0]*n
        trusts=[0]*n
        for i in trust:
            istrusted[i[1]-1]+=1
            trusts[i[0]-1]+=1
        for i in range(len(trusts)):
            if istrusted[i]==n-1 and trusts[i]==0:
                return i+1
        return -1
