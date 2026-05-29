class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        words=[]
        start=0
        s=s+' '
        for i in range(len(s)-1):
            if s[i]!=" " and s[i+1]==" ":
                words.append(s[start:i+1])
            if s[i]==" " and s[i+1]!=" ":
                start=i+1
            
        result=''
        for i in range(len(words)-1,-1,-1):
            if i==0:
                result+=words[i]
            else:
                result+=words[i]
                result+=' '
        return result

