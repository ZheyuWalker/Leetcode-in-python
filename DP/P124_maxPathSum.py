# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path = -1001

        def maxPathSubtrees(root):
            if root is None:
                return -1001

            left = maxPathSubtrees(root.left)
            right = maxPathSubtrees(root.right)

            up_max = max(root.val, root.val + left, root.val + right)
            curr_max = max(up_max, root.val + left + right)
            self.max_path = max(self.max_path, curr_max)

            return up_max

        maxPathSubtrees(root)

        return self.max_path