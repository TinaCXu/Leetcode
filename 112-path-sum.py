# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
sum = 22
-------------------------------------
root = 5
left_find_valid_path = self.hasPathSum(root.left, sum - root.val 17) <=
right_find_valid_path = self.hasPathSum(root.right, sum - root.val 17)
-------------------------------------
root = 4
left_find_valid_path = self.hasPathSum(root.left, sum - root.val 13) <=
right_find_valid_path = self.hasPathSum(root.right, sum - root.val 13)
-------------------------------------
root = 11
left_find_valid_path = self.hasPathSum(root.left, sum - root.val 2) 
right_find_valid_path = self.hasPathSum(root.right, sum - root.val 2) <=
-------------------------------------
root = 2
    sum == root.val

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # 如果遇到了叶子节点，返回上一层，应该返回什么
        if root == None:
            return False
        # 对于每一个root应该如何判断
        if root.left == None and root.right == None:
            if sum == root.val:
                return True
            else:
                return False
        # 应该如何迭代
        left_find_valid_path = self.hasPathSum(root.left, sum - root.val)
        right_find_valid_path = self.hasPathSum(root.right, sum - root.val)
        # 对于每一个中间节点应该如何传递至给上一层节点
        return left_find_valid_path or right_find_valid_path

# -------------------------
# root = 5
# left_sum = self.pathSum(root.left, sumUps) <-
# right_sum = self.pathSum(root.right, sumUps)
# sumUps.append(left_sum)
# sumUps.append(right_sum)
# -------------------------
# root = 4
# left_sum = self.pathSum(root.left, sumUps) <-
# right_sum = self.pathSum(root.right, sumUps)
# sumUps.append(left_sum)
# sumUps.append(right_sum)
# -------------------------
# root = 11
# left_sum = self.pathSum(root.left, sumUps) 7
# right_sum = self.pathSum(root.right, sumUps) 2<-
# sumUps = left_sum + right_sum + root 
# -------------------------
# root = 7
# left_sum = self.pathSum(root.left, sumUps) 0 <-
# right_sum = self.pathSum(root.right, sumUps) 0
# sumUps_left = left_sum + root 7
# sumUps_right = right_sum + root 7 
# -------------------------
# root = None
#     return 0

# class Solution:
#     def pathSum(self, root, sumUps):
#         if root == None:
#             return 0
#         left_sum = self.pathSum(root.left, sumUps)
#         right_sum = self.pathSum(root.right, sumUps)
#         sumUps.append(left_sum)
#         sumUps.append(right_sum)
        
#     def hasPathSum(self, root: TreeNode, sum: int) -> bool:
#         sumUps = []
#         self.pathSum(root, sumUps)
#         for sumup in sumUps:
#             if sumup == sum:
#                 return True
#             else:
#                 return False
            