class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        candies=[1]*n
        oldtotal=n
        total=n
        if n==1:
            return 1
        
        for i in range(n):
            if i-1>=0:
                if ratings[i-1]<ratings[i] and candies[i]<=candies[i-1]:
                    candies[i]=candies[i-1]+1 
                    total+=1    
            if i+1<n:
                if ratings[i+1]<ratings[i] and candies[i+1]>=candies[i]:
                    candies[i]=candies[i+1]+1
                    total+=1
        for i in range(n-1,-1,-1):
            if i-1>=0:
                if ratings[i-1]<ratings[i] and candies[i]<=candies[i-1]:
                    candies[i]=candies[i-1]+1 
                    total+=1    
            if i+1<n:
                if ratings[i+1]<ratings[i] and candies[i+1]>=candies[i]:
                    candies[i]=candies[i+1]+1
                    total+=1

        return sum(candies)


                

        

            
            


