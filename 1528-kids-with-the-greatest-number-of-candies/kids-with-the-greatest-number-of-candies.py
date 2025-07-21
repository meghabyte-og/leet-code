class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest=[]
        for i in range(len(candies)):
            candies[i]=candies[i]+extraCandies
            #print(candies)
            if candies[i]>=max(candies):
                greatest.append(True)
            else:
                greatest.append(False)
            candies[i]=candies[i]-extraCandies
        return greatest
        