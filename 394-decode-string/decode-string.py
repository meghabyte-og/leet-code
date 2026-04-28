class Solution:
    def decodeString(self, s: str) -> str:
        number=0
        string=''
        stack=[]
        flag=1
        for i in range(len(s)):
            print(number)
            if s[i].isnumeric():
                number=number*10+ int(s[i])
            if s[i]=='[':
                stack.append((string,number))
                number=0
                string=''
            if s[i].isalpha():
                string+=s[i]
            if s[i]==']':
                c,n=stack.pop()
                string=c+string*n
        return string
                
                

