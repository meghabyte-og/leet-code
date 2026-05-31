class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        if asteroids[0] > mass:
            return False
        for i in range(len(asteroids)): 
            if asteroids[i] > mass:
                return False
            mass = mass + asteroids[i]
        return True