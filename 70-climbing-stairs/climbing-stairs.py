class Solution:
    def climbStairs(self, n: int) -> int:
        # F(n) = F(n-1) + F(n-2)
        # F(1) = 1
        # F(2) = 2
        if n <= 2:
            return n
        f1 = 1
        f2 = 2
        f3 = 2
        for i in range(3, n+1):
            f3 = f1 + f2
            f1, f2 = f2, f3
        return f3