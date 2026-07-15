class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [0]*(len(s)+1)
        dp[0] = 1
        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j] == 0:
                    continue
                if s[j:i] in wordDict:
                    dp[i] = 1
                    break
        return bool(dp[-1])



