class Solution:
    def reverseWords(self, s: str) -> str:
        s=s+" "
        start=0
        words=[]
        for i in range(len(s)-1):
            if s[i]!=" " and s[i+1]==" ":
                words.append(s[start:i+1])
            if s[i]==" " and s[i+1]!=" ":
                start=i+1
        return ' '.join(words[::-1])