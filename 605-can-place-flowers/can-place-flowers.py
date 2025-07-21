class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        fb=[0]+flowerbed+[0]
        for i in range(1,len(flowerbed)+1):
            if fb[i-1]==fb[i]==fb[i+1]==0:
                fb[i]=1
                n=n-1
            if n<=0: return True
        return False