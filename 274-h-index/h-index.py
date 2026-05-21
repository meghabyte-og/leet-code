class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h=0
        for i in range(len(citations)):
            count=0 
            for j in range(len(citations)):
                if citations[j]>=citations[i]:
                    count+=1
            h=max(h,min(count,citations[i]))
        return h
