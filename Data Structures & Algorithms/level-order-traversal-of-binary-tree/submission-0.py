# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []

        q = collections.deque()
        q.append(root)

        # whole q empty -> done with whole tree 
        while q:
            # this is per level
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                # works with leaf nodes
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            # no empty levels
            if level:
                res.append(level)
        return res