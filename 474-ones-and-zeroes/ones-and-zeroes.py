class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {}
        def recurse(i, m, n):
            if i == 0:
                return 0
            if m  == 0 and n == 0:
                return 0
            if (i, m, n) in dp:
                return dp[(i, m, n)]
            zero = 0
            one = 0
            for s in strs[i-1]:
                if s == '0':
                    zero += 1
                else:
                    one += 1
            
            if zero <= m and one <= n:
                dp[(i,m,n)] = max(1 + recurse(i-1, m-zero, n-one), recurse(i-1, m, n))
            else:
                dp[(i,m,n)]  = recurse(i-1, m, n)
            return dp[(i,m,n)] 
        return recurse(len(strs), m, n)
                 