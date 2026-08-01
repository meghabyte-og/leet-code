class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2 != 0:
            return False
        n = len(nums)
        s = int(s/2)
        dp = [[False]*(s+1) for _ in range(n+1)]
        for i in range(len(dp)):
            dp[i][0] = True
        
        for i in range(1, n+1):
            for j in range(1, s+1):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
