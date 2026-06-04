class Solution(object):
    def totalWaviness(self, num1, num2):
        c=0
        for i in range(num1,num2+1):
            j=str(i)
            for k in range(1,len(j)-1):
                if j[k]>j[k+1] and j[k]>j[k-1]:
                    c=c+1
                    continue
                if j[k]<j[k+1] and j[k]<j[k-1]:
                    c=c+1
                    continue
        return c