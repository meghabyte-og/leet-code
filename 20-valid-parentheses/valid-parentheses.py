class Solution:
    def isValid(self, s: str) -> bool: 
        stack=[]
        d={'}':'{',']':'[',')':'('}
        for i in range(len(s)):
            if s[i] in {'(','{','['}:
                stack.append(s[i])
            else:
                if len(stack)==0:
                    return False
                top=stack.pop()
                if d[s[i]]!=top:
                    stack.append(top)
                    stack.append(s[i])
        if len(stack)==0:
            return True
        return False
