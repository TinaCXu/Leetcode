# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def _minDepth(self,root):
        if root == None:
            return 99999
        if root.left == None and root.right == None:
            return 1
        return min(self._minDepth(root.left),self._minDepth(root.right))+1
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return self._minDepth(root)