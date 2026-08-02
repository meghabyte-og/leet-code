class Solution:
    def stoneGame(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        dp = [[0]* (len(nums)+1) for _ in range(len(nums)+1)]
        def recurse(start, end):
            if start > end:
                return 0
            if dp[start][end] != 0:
                return dp[start][end]
            dp[start][end] = max(nums[start] - recurse(start+1, end), nums[end] - recurse(start, end-1))  
            return dp[start][end]            
        return True if recurse(0, len(nums)-1)>=0 else False

                
            
