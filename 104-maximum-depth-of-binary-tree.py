# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    cnt_left = 1
    cnt_right = 1
    depth = []
    def getDepth(self, root, depth):
        if root == None:
            cur_depth = [cnt_left, cnt_right]
            depth.append(cur_depth)
            return 
        getDepth(root.left, depth)
        ans.append(root.val)
        getDepth(root.right, depth)
        cnt_left += 1
        cnt_right += 1 

    def maxDepth(self, root: TreeNode) -> int:
        getDepth(root, depth)
        ans = max(depth)
        return ans