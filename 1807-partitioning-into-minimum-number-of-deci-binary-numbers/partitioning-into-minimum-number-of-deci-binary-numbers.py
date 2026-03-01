class Solution:
    def minPartitions(self, n: str) -> int:
        m=0
        for i in n:
            if int(i)>m:
                m=int(i)
        return m
