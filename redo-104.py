# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

    3
   / \
  9  20
    /  \
   15   7

-----------------------------
root = 3
left_depth = self.maxDepth(root.left) 1
right_depth = self.maxDepth(root.right) 2<=
return max(left_depth, right_depth) + 1
-----------------------------
root = 20
left_depth = self.maxDepth(root.left) 1 <=
right_depth = self.maxDepth(root.right) 1 <=
return max(left_depth, right_depth) + 1 2
-----------------------------
root = None
    return 0

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # step1:如果遇到了叶子节点，返回上一层，应该返回什么
        if root == None:
            return 0
        # step2:对于每一个节点，应该如何判断(其实不需要这一步，可以看看能不能和传递上一层节点合并)
        if root.left == None and root.right == None:
            return 1
        # step3:如何迭代：值传递
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        # step4:对于每一个中间节点应该如何传递至给上一层节点
        return max(left_depth, right_depth) + 1
