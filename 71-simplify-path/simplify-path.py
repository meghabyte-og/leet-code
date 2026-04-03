class Solution:
    def simplifyPath(self, path: str) -> str:
        subpath=[]
        stack=''
        count_slash=0
        count_dot=0
        path=path+'/'
        for i in range(len(path)):
            if path[i]=='/':
                if stack=='':
                    continue
                elif stack=='..':
                    if len(subpath)>0:
                        subpath.pop()
                    stack=''
                else:
                    if stack!='.':
                        subpath.append(stack)
                stack=''
            else:
                stack+=path[i]
        ans='/'
        # print(subpath)
        
        for i in range(len(subpath)):
            if i==len(subpath)-1:
                ans+=subpath[i]
            else:
                ans+=subpath[i]+'/'
        return ans

