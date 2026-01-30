class Solution:
    def tribonacci(self, n: int) -> int:
        t1=0
        t2=1
        t3=1
        if n<3:
            if n==0:
                return 0
            else:
                return 1
        for _ in range(3,n+1):
            t1,t2,t3=t2,t3,(t1+t2+t3)
        return t3