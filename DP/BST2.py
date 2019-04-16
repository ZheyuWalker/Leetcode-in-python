# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if not n: return []
        return self.cTree(1, n+1)
        
    def cTree(self, begin: int, end: int) -> List[TreeNode]:
        if not (end-begin): return [None]
        rlt = []
        for i in range(begin, end):
            left_sub = self.cTree(begin, i)
            right_sub = self.cTree(i+1, end)
            for l in left_sub:
                for r in right_sub:
                    root = TreeNode(i)
                    root.left, root.right = l, r
                    rlt.append(root)
        return rlt
