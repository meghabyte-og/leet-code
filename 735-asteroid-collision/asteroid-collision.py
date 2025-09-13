class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for asteroid in asteroids:
            stack.append(asteroid)
            while len(stack)>1 and stack[-1]<0 and stack[-2]>0:
                neg=abs(stack.pop())
                pos=stack.pop()
                if neg>pos:
                    stack.append(-neg)
                if pos>neg:
                    stack.append(pos)
        return stack
            
            
