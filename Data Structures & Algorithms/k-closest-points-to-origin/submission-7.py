import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def compute_distance(x1, y1, x2, y2):
            return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        
        distances = [(compute_distance(x, y, 0, 0), [x, y]) for x, y in points]

        heapq.heapify(distances)

        res = []
        while k > 0:
            res.append(heapq.heappop(distances)[1])
            k -= 1

        return res