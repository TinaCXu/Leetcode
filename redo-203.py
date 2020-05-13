# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#    1->2->6->3->4->5->6
# p  c  n
#       h
#       p     c  n

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # initiate
        prev = None
        cur = head
        while cur != None:
            if cur.val == val:
                if prev == None:
                    head = head.next
                # prev !== None
                else:
                    prev.next = cur.next
            # cur.val !== val
            else:
                prev = cur
            cur = cur.next
        return head
