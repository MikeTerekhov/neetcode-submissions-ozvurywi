# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # empty subtree -> technically yes
        if not subRoot: return True
        # ORDER MATTERS ->  t not empty at this point
        if not root: return False

        if self.sameTree(root, subRoot): return True

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)) 

    def sameTree(self, s, t):
        # both empty
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return (self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right))

        # one is empty and another is not, obvi cannot be the same
        return False
