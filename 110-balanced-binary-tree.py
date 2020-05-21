# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def _isBalanced(self, root):
        # 如果遇到了叶子节点，返回上一层，应该返回什么
        if root == None:
            return 0, True
        # 应该如何迭代
        leftHeight, left_isBalanced = self._isBalanced(root.left)
        rightHeight, right_isBalanced = self._isBalanced(root.right)
        # 对于每一个root应该如何判断
        if left_isBalanced == False or right_isBalanced == False or abs(leftHeight - rightHeight) > 1:
            return 0, False
        # else:
            # return max(left_isBalanced, right_isBalanced) + 1, left_isBalanced and right_isBalanced
        # 对于每一个中间节点应该如何传递至给上一层节点
        return max(leftHeight, rightHeight) + 1, left_isBalanced and right_isBalanced
    def isBalanced(self, root: TreeNode) -> bool:
        height, balanced = self._isBalanced(root)
        return balanced





# class Solution:
#     def isBalanced(self, root: TreeNode) -> bool:
#         if root == None:
#             return 0
#         if root.left == None and root.right == None:
#             return 1
#         left_depth = self.isBalanced(root.left)
#         right_depth = self.isBalanced(root.right)
#         max_depth = max(left_depth, right_depth) + 1
#         min_depth = min (left_depth, right_depth) + 1
#         if max_depth - min_depth <= 1:
#             return True
#         else:
#             return False
        