class Solution:   
    def isSame(self, r: Optional[TreeNode], s: Optional[TreeNode]) -> bool:
        if not r and not s: return True
        if not r or not s: return False
        return r.val == s.val and self.isSame(r.left, s.left) and self.isSame(r.right, s.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False
        
        if self.isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)