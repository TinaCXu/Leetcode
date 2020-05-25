# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

        4
       / \
      2   7
     / \
    1   3

----------------
root = 4
self.searchBST(root.left, val) <=
self.searchBST(root.right, val)
----------------
root = 2
return root

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # 如果遇到了叶子节点，返回上一层，应该返回什么
        if root == None:
            return
        # 对于每一个root应该如何判断
        if root.val == val:
            return root
        # 应该如何迭代 & 引用传递
        self.searchBST(root.left, val)
        self.searchBST(root.right, val)