# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        cur = node
        Next = cur.next
        # change the value of cur
        cur.val = Next.val
        # change the next of cur
        cur.next = Next.next