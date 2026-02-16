class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]
        sub=[]
        nums=[i+1 for i in range(n)]
        def recurse(i):
            if len(sub)==k:
                result.append(sub[:])
                return
            if i>=n:
                return
            sub.append(nums[i])
            recurse(i+1)
            sub.pop()
            recurse(i+1)

            
        recurse(0)
        return(result)
            
