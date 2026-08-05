class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = ord(s1[i-1]) + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        lcs = dp[-1][-1]
        total = 0
        for s in s1:
            total += ord(s)
        for s in s2:
            total += ord(s)
        
        return total - 2*(lcs)