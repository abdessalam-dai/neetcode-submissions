from collections import deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {i: [] for i in range(numCourses)}
        indegrees = [0] * numCourses
        
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            indegrees[dest] += 1
            
        queue = deque([])
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
                
        res = []
        
        while queue:
            curr = queue.popleft() 
            res.append(curr)
            
            # Check all courses that depend on the current course
            for neighbor in adj_list[curr]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
                    
        if len(res) == numCourses:
            return res
        else:
            return []