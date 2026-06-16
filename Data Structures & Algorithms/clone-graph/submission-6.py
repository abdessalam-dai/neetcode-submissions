"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited={}
        def dfs(node):
            if node in visited:
                return visited[node]
            
            cloneNode = Node(val=node.val)
            visited[node] = cloneNode

            for child in node.neighbors:
                cloneNode.neighbors.append(dfs(child))

            return cloneNode
        return dfs(node) if node else None