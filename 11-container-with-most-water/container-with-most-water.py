class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_volume=0
        i=0
        j=len(height)-1
        while i<j:
            volume=min(height[i],height[j])*(j-i)
            if volume>max_volume:
                max_volume=volume
            if height[i]>height[j]:
                j=j-1
            else:
                i=i+1
        return max_volume
