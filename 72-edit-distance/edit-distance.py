class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        def recurse(i, j):
            if i == 0:
                return j
            if j == 0:
                return i

            if dp[i][j] != 0:
                return dp[i][j]

            if word1[i-1] == word2[j-1]:
                dp[i][j] = recurse(i-1, j-1)
            
            else:
                dp[i][j] = 1 + min(
                    recurse(i, j-1),
                    recurse(i-1, j),
                    recurse(i-1, j-1)
                )
            return dp[i][j]
        return recurse(m,n)
