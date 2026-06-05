class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency = {}
        for i in range(len(s)):
            if s[i] not in frequency: 
                frequency[s[i]] = 1
            else:
                frequency[s[i]] +=1
        for i in range(len(s)):
            if frequency[s[i]] == 1:
                return i
        return -1