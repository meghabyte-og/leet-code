class Solution:
    def minInsertions(self, s: str) -> int:
        srev = s[::-1]
        n = len(s)
        dp = [[0]*(n+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == srev[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        lcs = dp[-1][-1]

        return n-lcs