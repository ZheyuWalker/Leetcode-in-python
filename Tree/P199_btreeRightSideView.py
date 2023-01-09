# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes
# you can see ordered from top to bottom.

# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return res
        q = deque()
        q.append((root, 1))
        while len(q):
            node, depth = q.popleft()
            if depth > len(res):
                res.append(node.val)
            if node.right:
                q.append((node.right, depth+1))
            if node.left:
                q.append((node.left, depth+1))
        return res