# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        nodes = [root]
        res = 0
        while nodes:
            node = nodes.pop()
            if node:
                v = node.val
                if v > high:
                    nodes.append(node.left)
                elif v < low:
                    nodes.append(node.right)
                else:
                    res += v
                    nodes.append(node.right)
                    nodes.append(node.left)
        return res
