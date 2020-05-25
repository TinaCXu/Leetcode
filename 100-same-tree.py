# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
        1
      2   3
    4       5
treeSe = [1,2,4,#,#,#,3,#,5,#,#]

[1,2,#,#,3,#,#]
   1
  2 3


---------
root = 1
treeSe.append(root.val) 1 
self.treeSequence(root.left, treeSe) <=
self.treeSequence(root.right, treeSe)
---------
root = 2
treeSe.append(root.val) 2 
self.treeSequence(root.left, treeSe) <=
self.treeSequence(root.right, treeSe)
---------
root = 4
treeSe.append(root.val) 4 
self.treeSequence(root.left, treeSe) #<=
self.treeSequence(root.right, treeSe) #<=
-------
if root == None:
    treeSe.append('#')
    return


class Solution:
    def treeSequence(self, root: TreeNode): # return list
        # 如果遇到了叶子节点，返回上一层，应该返回什么
        if root == None:
            return ['#']
        
        ret = [root.val]
        left_seq = self.treeSequence(root.left)
        right_seq = self.treeSequence(root.right)
        for item in left_seq:
            ret.append(item)
        for item in right_seq:
            ret.append(item)
        return ret
        [1,[2,3],[4,5]]
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # treeSe1 = []
        # treeSe2 = []
        treeSe1 = self.treeSequence(p)
        treeSe2 = self.treeSequence(q)
        if len(treeSe1) != len(treeSe2):
            return False
        #len is equal
        for i in range(0,len(treeSe1)):
            if treeSe1[i] != treeSe2[i]:
                return False
        #pass above two, len is equal, every position is equal.
        return True


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 如果遇到了叶子节点，返回上一层，应该返回什么
        # 对于每一个root应该如何判断
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val：
            return False
        # 应该如何迭代 & 引用传递
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)