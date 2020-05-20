# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
       1
     2    3
   4     6  7
             8

---------
root = 1
left_depth = self.getDepth(root.left) 2
right_depth = self.getDepth(root.right) 3<-
return 4
---------


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        # what do i need
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1
