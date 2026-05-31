class Solution:
    def numTilings(self, n: int) -> int:
        # n= 1,2,3,4,5,6,7
        # numTilings(n) = 1,2,5,11,24,53,117
        if n <=2:
            return n
        dp = [0] * n 
        dp[0] = 1
        dp[1] = 2
        dp[2] = 5
        for i in range(3, len(dp)):
            dp[i] = 2*dp[i-1] + dp[i-3]
        return dp[-1]%(10**9 + 7)

    