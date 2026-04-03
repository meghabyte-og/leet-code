class Solution:
    def isValid(self, s: str) -> bool:
        #([]{}) 
        #([ not valid
        #([] [] valid pop 
        stack=[]
        for i in range(len(s)):
            stack.append(s[i])
            while len(stack)>1:
                second=stack.pop()
                first=stack.pop()
                if (first=='[' and second!=']') or (first=='{' and second!='}') or (first=='(' and second!=')') or (first in {')',']','}'}) :
                    stack.append(first)
                    stack.append(second)
                    break
        if len(stack)==0:
            return True
        else:
            return False
            
                    

