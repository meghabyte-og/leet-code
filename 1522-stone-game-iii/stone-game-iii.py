class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = [0]*(len(stoneValue)+1)
        stoneValue = stoneValue[::-1]
        def recurse(i):
            if i == 0:
                return 0

            if dp[i] != 0:
                return dp[i]

            elif i == 1:
                dp[i] = (stoneValue[i-1])

            if i == 2:
                dp[i] = max(
                    stoneValue[i-1] + stoneValue[i-2] - recurse(i-2),
                    stoneValue[i-1] - recurse(i-1))
            
            if i >= 3:
                dp[i] = max(
                    stoneValue[i-3] + stoneValue[i-1] + stoneValue[i-2] - recurse(i-3),
                    stoneValue[i-1] + stoneValue[i-2] - recurse(i-2),
                    stoneValue[i-1] - recurse(i-1)
                )
                
            return dp[i]

        result = recurse(len(stoneValue))

        if result == 0:
            return 'Tie'
        elif result > 0:
            return 'Alice'
        else:
            return 'Bob'
            