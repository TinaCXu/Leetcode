s = "12345"

num = 0

for digit in s:
    num *= 10 # 10, 120, 1230, 12340
    num += digit # 12, 123, 1234, 12345
print (num)

#1
#num
# 10
# 10000
#  2000
#   300
#    40
#     5

# 1  0 1 1 0
# 16 8 4 2 1
= 2 * 1 + 4 * 1 + 16 * 1 = 22
# 1  0 1 1 1
= 23
# 1  1 0 0 0
= 16 + 8 = 24

# 10000   1000  100   10 1

for digit in s:
    num *= 10 # 10, 120, 1230, 12340
    num += digit # 12, 123, 1234, 12345
print (num)

s = "10110"
         1 0
# 16 8 4 2 1
   1 0 1 1 0 
for digit in s:
    num *= 2 # 0, 10, 100, 1010, 10110
    num += digit # 1, 10, 101, 1011, 10110
print (num)

    num *= 2 # 0, 10:2, 100:4, 1010:10, 10110:22
    num += digit # 1, 10:2, 101:5, 1011:11, 10110:22

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        cur = head
        num = 0
        while cur != None:
            num *= 2
            num += cur.val
            cur = cur.next
        return num