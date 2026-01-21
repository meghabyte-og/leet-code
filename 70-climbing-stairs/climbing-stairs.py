class Solution:
    def climbStairs(self, n: int) -> int:
        # 1-> 1
        # 2-> 2
        # 3-> 3
        # 4-> 5
        # 5-> 8
        if n<=3:
            return n
        a=2
        b=3
        for _ in range(3,n):
            a,b=b,a+b
        return b
            
        
