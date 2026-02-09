class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        a=0
        n=len(candidates)
        subsets=[]
        current=[]
        s=sum(candidates)
        def sub(a,i):
            if a==target:
                subsets.append(current[:])
                return
            if a>target:
                return
            if i>=n:
                return
            sub(a,i+1)
            a=a+candidates[i]
            current.append(candidates[i])
            sub(a,i)
            a=a-candidates[i]
            if current:
                current.pop()
            
                    
        sub(a,0)
        return subsets

            


                



