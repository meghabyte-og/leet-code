class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        p1=0
        p2=len(s)-1
        vowel=['a','e','i','o','u']
        while p1<p2:
            if s[p1].lower() in vowel and s[p2].lower() in vowel:
                s[p1],s[p2]=s[p2],s[p1]
                p1=p1+1
                p2=p2-1
            elif s[p1].lower() not in vowel:
                p1=p1+1
            else:
                p2=p2-1
        return ''.join(s)            
            

