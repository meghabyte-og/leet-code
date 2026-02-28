class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # so basically all the permutations of all letters of the given numbers
        letters={2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        letter=[]
        for i in digits:
            letter.append(letters[int(i)])
        n=len(digits)
        ans=[]
        def dfs(i,subset):
            if i==n:
                ans.append(''.join(subset))
                return
            
            for chars in letter[i]:
                subset.append(chars)
                dfs(i+1,subset)
                subset.pop()
        dfs(0,[])
        return ans
            
            
