class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=[]
        i=0
        j=0
        n=len(s)
        while j<n:
            if s[j]==' ':
                words.append(s[i:j])
                i=j+1
            if j==n-1:
                words.append(s[i:j+1])
            j=j+1
        j=0
        unique_words={}
        unique_pattern={}
        for i in words:
            if i in unique_words:
                continue
            unique_words[i]=j+1
            j=j+1
        j=0
        for i in pattern:
            if i in unique_pattern:
                continue
            unique_pattern[i]=j+1
            j=j+1
        print(unique_words)
        print(unique_pattern)
        pattern_compare=[]
        string_compare=[]
        for i in words:
            string_compare.append(unique_words[i])
        for i in pattern:
            pattern_compare.append(unique_pattern[i])
        if string_compare==pattern_compare:
            return True
        else:
            return False






