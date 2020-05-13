# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#     [ 1, 2, 3, 4, 5]
#          c
# cnt   1  2
# ind   0

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # initiate
        cur = head
        cnt = 0
        # get the length of ListNode
        while cur != None:
            cnt += 1
            cur = cur.next
        # get the middle_index
        middle_index = cnt // 2
        # get the index and return middle point
        cur = head
        index = 0
        while cur != None:
            if index == middle_index:
                return cur
            cur = cur.next
            index += 1