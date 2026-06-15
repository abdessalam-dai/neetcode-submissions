# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return True, 0
            
            r_balanced, r_h = dfs(root.right)
            l_balanced, l_h = dfs(root.left)
            
            return r_balanced and l_balanced and abs(l_h - r_h) <= 1, 1 + max(r_h, l_h)
        return dfs(root)[0]