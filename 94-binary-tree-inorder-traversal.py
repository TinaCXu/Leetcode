# [A,B,C,D,null]


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

A = TreeNode(10)
B = TreeNode(5)
C = TreeNode(15)
D = TreeNode(3)
E = TreeNode(12)
F = TreeNode(18)
   1 = 1   1
  10 = 2   2
 100 = 4   3
1000 = 8   4(n)

2^4 - 1 = 15

10000 - 1 = 1111 = 15

10000 - 1 = 1111 = 15

1....0 (x个0) - 1 = 1....1(x)


    



        10
     5         15
 4     6    12    18

中序root在中间访问：4, 5, 6, 10, 12, 15, 18
前序root在前访问：10, 5, 4, 6, 15, 12, 18
后序root在后访问：4, 6, 5, 12, 18, 15, 10

random access, log_2(n)
insert,
delete,

A.left = B
A.right = C
B.left = D
C.left =  E
C.right = F
        10
     5         15
 4     6    12    18
class Solution:
    ans = []
    def getInorder(root):
        if root == None:
            return
        getInorder(root.left)
        ans.append(root.val)
        getInorder(root.right) 
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        getInorder(root)
        return ans

    def getInorder(root, ans):
        if root == None:
            return
        getInorder(root.left, ans)
        ans.append(root.val)
        getInorder(root.right, ans) 

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        getInorder(root, ans)
        print (ans)
        return ans
        10
     5         15
 4     6    12    18

 -------------------------
root = 10
left_ans = getInorder(root.left) [4,5,6]<-
right_ans = getInorder(root.right) [12,15,18]

current_ans = []
for item in left_ans:
    current_ans.append(item)
current_ans.append(root.val)
for item in right_ans:
    current_ans.append(item)
return current_ans
[4,5,6,10,12,15,18]

-----------------------------

    def getInorder(root):#return inorder traversal
        if root == None:
            return []

        left_ans = getInorder(root.left)
        right_ans = getInorder(root.right) 
        
        current_ans = []
        for item in left_ans:
            current_ans.append(item)
        current_ans.append(root.val)
        for item in right_ans:
            current_ans.append(item)
        return current_ans
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return getInorder(root)

class Solution:
    def _minDepth(self, root):
        if root == None:
            return 999999
        if root.left == None and root.right == None:
            return 1
        return min(self._minDepth(root.left),  self._minDepth(root.right)) + 1
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return self._minDepth(root)