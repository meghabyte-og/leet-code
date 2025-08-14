class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxv=0
        c=0
        vowels={'a','e','i','o','u'}
        window=s[:k] #012
        for i in window:
            if i in vowels:
                c=c+1
        maxv=c
        
        for i in range(k,len(s)):
            
            if s[i] in vowels:
                c=c+1
            if s[i-k] in vowels:
                c=c-1
            maxv=max(c,maxv)
            
        return maxv
            

            

            


            
