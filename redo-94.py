# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
   1
    \
     2
    /
   3
---------
root = 1
# 不可以对引用传递进行轮轮赋值，因为引用传递只传递地址，是实时变化的，直接执行
left = self._inorderTraversal(root.left, ans) 
right = self._inorderTraversal(root.right, ans) <-
ans.append(left)
ans.append(root.val)
ans.append(right)
print(ans)
return ans
---------
root = 2
left = self._inorderTraversal(root.left, ans) [3]
right = self._inorderTraversal(root.right, ans) <-
ans.append(left) [3]
ans.append(root.val)
ans.append(right)
print(ans)
return ans
---------
root = None

class Solution:
    def _inorderTraversal(self, root, ans):
        # 如果遇到了叶子节点，返回上一层，应该返回什么
        if root == None:
            return
        # 对于每一个节点，应该如何判断(与子节点合并)
            # *应该如何迭代
            left = self._inorderTraversal(root.left, ans)
            right = self._inorderTraversal(root.right, ans)
            # *对于每一个中间节点应该如何传递至给上一层节点（对于引用传递不存在这一步，因为迭代和传递是同时的！！！）
            if left != None:
                ans.append(left)
            ans.append(root.val)
            if right != None:
                ans.append(right)
            print(ans)
            return ans

        # *更新：引用传递，合并迭代和传递
        self._inorderTraversal(root.left, ans)
        ans.append(root.val)
        self._inorderTraversal(root.right, ans)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 传入参数
        ans = []
        # 执行函数
        self._inorderTraversal(root, ans)
        return ans
