class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        maxvol=0
        while i<=j:
            vol=(j-i)*min(height[i],height[j])
            if vol>maxvol:
                maxvol=vol
        # when to incremenet i and decremenet j?
            if height[i]>height[j]:
                j=j-1
                continue
            if height[i]<height[j]:
                i=i+1
                continue
            if height[i]==height[j]:
                i=i+1
                continue
        return maxvol
