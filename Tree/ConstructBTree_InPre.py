# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        '''
        # Recursive
        n = len(preorder)
        if n != len(inorder) or n == 0:
            return
        
        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)
        
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root
        '''
        
        # Iterative
        
