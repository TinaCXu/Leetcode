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
    def getInorder(root, ans):
        if root == None:
            return
        getInorder(root.left, ans)
        ans.append(root.val)
        getInorder(root.right, ans) 

----------
root = 10
getInorder(root.left, ans) 
ans.append(root.val)
getInorder(root.right, ans) <-
    


ans=[4, 5, 6, 10, ]
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        getInorder(root, ans)
        print (ans)
        return ans