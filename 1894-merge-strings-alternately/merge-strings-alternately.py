class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        list_a = list(word1)
        list_b = list(word2)
        a=len(word1)
        b=len(word2)
        merged=list()
        for i in range(a if a>b else b):
            if i<a:
                merged.append(list_a[i])
            if i<b:
                merged.append(list_b[i])
        merged=''.join(merged)
        #print(merged)
        return(merged)