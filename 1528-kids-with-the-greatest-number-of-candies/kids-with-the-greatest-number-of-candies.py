class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest=[]
        m=max(candies) #we only need to check if the max is greater than the max of existing array
        return[extraCandies+i>=m for i in candies]
        