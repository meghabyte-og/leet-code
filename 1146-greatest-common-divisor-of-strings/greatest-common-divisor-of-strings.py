class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        g= math.gcd(len(str1),len(str2))
        if(str1== str1[0:g]*(len(str1)//g) and str2== str1[0:g]*(len(str2)//g)):
            return(str1[0:g])
        else: return ""
        
        