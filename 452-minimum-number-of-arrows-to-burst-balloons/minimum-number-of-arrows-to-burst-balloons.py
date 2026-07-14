class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points)
        print(points)
        prev = points[0][1]
        count = 1
        for i in range(1, len(points)):
            if points[i][0] <= prev:
                prev = min(prev, points[i][1])
                continue
            prev = points[i][1]
            count += 1
        return count