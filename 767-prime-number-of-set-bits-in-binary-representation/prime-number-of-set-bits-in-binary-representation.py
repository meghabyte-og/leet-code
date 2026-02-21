class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        result=0
        def isPrime(n: int)->bool:
            if n==0 or n==1:
                return False
            if n==2:
                return True
            c=0
            for i in range(1,n+1):
                if n%i==0:
                    c+=1
                if c>2:
                    return False
            return True 

        def toBinary(n: int)->int:
            c=0
            while n>0:
                r=n%2
                n=int(n/2)
                if r==1:
                    c+=1
            return c

        for i in range(left,right+1):
            one_count=toBinary(i)
            print(one_count)
            if isPrime(one_count):
                result+=1
        return result
            