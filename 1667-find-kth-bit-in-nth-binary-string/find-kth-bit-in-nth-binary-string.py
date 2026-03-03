class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        b='0'
        for j in range(n-1):
            b=b+'1'+''.join(['1' if i == '0' else '0' for i in b[::-1]])
        return b[k-1]
        
        