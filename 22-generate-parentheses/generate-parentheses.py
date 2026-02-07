class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def check(p,openp,closep):
            if len(p)==2*n:
                result.append(p)
                return
            if openp<n:
                check(p+'(',openp+1,closep)
            if closep<openp:
                check(p+')',openp,closep+1)
        check('',0,0)
        return result





