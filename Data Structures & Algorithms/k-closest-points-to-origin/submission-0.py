import heapq
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [(-sqrt(x ** 2 + y ** 2), x, y) for x, y in points]
        h = points[:k]
        heapq.heapify(h)
        for i in range(k, len(points)):
            heapq.heappushpop(h, points[i])
        return [[x, y] for d, x, y in h]