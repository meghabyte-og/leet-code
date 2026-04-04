class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            if tokens[i] not in ('+','-','/','*'):
                stack.append(tokens[i])
                continue
            second=int(stack.pop())
            first=int(stack.pop())
            if tokens[i]=='+':
                stack.append(first+second)
            if tokens[i]=='-':
                stack.append(first-second)
            if tokens[i]=='*':
                stack.append(first*second)
            if tokens[i]=='/':
                stack.append(first/second)
        return int(stack[0])