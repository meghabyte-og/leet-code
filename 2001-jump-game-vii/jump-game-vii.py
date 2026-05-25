class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [0]* n
        dp[0] = 1
        prefix = [0]*(n+1)
        prefix[1] = 1
        for i in range(1,n):
            if s[i] == '1':
                prefix[i+1] = prefix[i]
                continue
            left = max(0, i- maxJump)
            right =i-minJump
            if right>=0:
                reach= prefix[right+1]- prefix[left]
                if reach >0 :
                    dp[i]=1
           
            prefix[i+1] = prefix[i] + dp[i]
        if dp[-1]==1:
            return True
        else:
            return False
        

  

        
                

            

            
                

            