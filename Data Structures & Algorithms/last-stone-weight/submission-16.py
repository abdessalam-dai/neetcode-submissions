import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 1. Create the max-heap by inverting the values
        heap = [-x for x in stones]
        heapq.heapify(heap)

        # 2. Smash stones until 0 or 1 remains
        while len(heap) > 1:
            x = -heapq.heappop(heap)  # Largest stone
            y = -heapq.heappop(heap)  # Second largest stone
            
            if x != y:
                heapq.heappush(heap, -(x - y)) # Push the remainder back
        
        # 3. Return 0 if heap is empty, else return the absolute value of the last element
        return -heap[0] if heap else 0

