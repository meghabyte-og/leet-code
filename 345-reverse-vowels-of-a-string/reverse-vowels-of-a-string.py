class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel=[]
        s=list(s)
        for i in s:
            if i.lower()=='a' or i.lower()=='e' or i.lower()=='i' or i.lower()=='o' or i.lower()=='u':
                vowel.append(i)
        #vowel=vowel[::-1]
        for i in range(len(s)):
            if s[i].lower()=='a' or s[i].lower()=='e' or s[i].lower()=='i' or s[i].lower()=='o' or s[i].lower()=='u':
                s[i]=vowel[len(vowel)-1]
                vowel.pop(len(vowel)-1)
        return ''.join(s)

