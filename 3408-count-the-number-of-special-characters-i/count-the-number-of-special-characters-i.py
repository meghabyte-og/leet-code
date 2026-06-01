class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = set()
        upper = set()
        count = 0
        for i in range(len(word)):
            if word[i].islower():
                lower.add(word[i])
            else:
                upper.add(word[i].lower())
        for u in upper:
            if u in lower:
                count += 1
        return count