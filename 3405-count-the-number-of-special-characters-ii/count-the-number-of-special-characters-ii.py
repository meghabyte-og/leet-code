class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        letters=set()
        for i in word:
            if i.lower() not in letters:
                letters.add(i)
        #store the last index of lower
        #first index of upper
        upper={}
        lower={}
        count=0
        for i in range(len(word)):
            if word[i].islower():
                lower[word[i]]=i
                continue
            if word[i].isupper():
                if word[i].lower() in upper:
                    continue
                else:
                    upper[word[i].lower()]=i
        print(upper)
        print(lower)
        for i in letters:
            if i in upper and i in lower and upper[i]>lower[i]:
                count+=1
        return count
        

            
                


            

            
