class Solution:
    def largestGoodInteger(self, num: str) -> str:
        num=num+" "
        goodinteger="-1"
        for i in range(len(num)-3):
            print(num[i],num[i+1],num[i+2])
            print(goodinteger)
            if num[i]==num[i+1]==num[i+2]:
                if int(goodinteger)<int(num[i:i+3]):
                    goodinteger=num[i:i+3]
        if goodinteger!='-1':
            return goodinteger
        else:
            return ""
        