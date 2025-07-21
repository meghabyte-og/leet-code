class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return[extraCandies+i>=max(candies) for i in candies]
        