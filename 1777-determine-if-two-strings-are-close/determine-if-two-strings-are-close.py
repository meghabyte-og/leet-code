class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1={}
        count2={}
        for i in word1:
            if i not in count1:
                count1[i]=1
            else:
                count1[i]+=1
        for i in word2:
            if i not in count2:
                count2[i]=1
            else:
                count2[i]+=1
        if sorted(list(count1.values()))==sorted(list(count2.values())) and sorted(list(count1.keys()))==sorted(list(count2.keys())):
            return True
        else :
            return False