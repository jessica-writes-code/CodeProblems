class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()

        arrows, i = 1, 0
        while i < (len(points) - 1):
            if points[i][1] >= points[i + 1][0]:
                points[i + 1][1] = min(points[i][1], points[i + 1][1])
            else:
                arrows += 1
            i += 1

        return arrows
