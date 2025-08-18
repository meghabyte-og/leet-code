class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences={}
        for i in arr:
            if i in occurences: 
                occurences[i]= occurences[i]+1
            else:
                occurences[i]=1
        return False if len(set(occurences.values()))<len(occurences) else True