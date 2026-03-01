class Solution:
    def minPartitions(self, n: str) -> int:
        n=sorted(n)
       
        return int(n[len(n)-1])
