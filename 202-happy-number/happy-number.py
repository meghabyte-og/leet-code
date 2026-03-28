class Solution:
    def isHappy(self, n: int) -> bool:
        n=str(n)
        while len(n)>1:
            s=0
            for i in n:
                s+=int(i)**2
            n=str(s)
            # print(n)
        if int(n)==1 or int(n)==7:
            return True
        else:
            return False

                

