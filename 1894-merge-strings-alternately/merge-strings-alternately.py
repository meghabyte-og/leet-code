class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ""
        m = len(word1)
        n = len(word2)
        for i in range(min(m,n)):
            answer = answer + word1[i]
            answer = answer + word2[i]
        
        answer = answer + (word1[n:] if m > n else word2[m:])
        return answer
        
